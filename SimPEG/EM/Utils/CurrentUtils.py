import numpy as np
from SimPEG import Utils


def line(a, t, l):
    """
        Linear interpolation between a and b
        0 <= t <= 1
    """
    return a + t * l


def weight(t, a1, l1, h1, a2, l2, h2):
    """
        Edge basis functions
    """
    x1 = line(a1, t, l1)
    x2 = line(a2, t, l2)
    w0 = (1. - x1 / h1) * (1. - x2 / h2)
    w1 = (x1 / h1) * (1. - x2 / h2)
    w2 = (1. - x1 / h1) * (x2 / h2)
    w3 = (x1 / h1) * (x2 / h2)
    return np.r_[w0, w1, w2, w3]


# TODO: Extend this when current is defined on cell-face
def getStraightLineCurrentIntegral(hx, hy, hz, ax, ay, az, bx, by, bz):
    """
      Compute integral int(W . J dx^3) in brick of size hx x hy x hz
      where W denotes the 12 local bilinear edge basis functions
      and where J prescribes a unit line current
      between points (ax,ay,az) and (bx,by,bz).
    """

    # length of line segment
    lx = bx - ax
    ly = by - ay
    lz = bz - az
    l = np.sqrt(lx**2+ly**2+lz**2)

    if l == 0:
        sx = np.zeros(4, 1)
        sy = np.zeros(4, 1)
        sz = np.zeros(4, 1)

    # integration using Simpson's rule
    wx0 = weight(0., ay, ly, hy, az, lz, hz)
    wx0_5 = weight(0.5, ay, ly, hy, az, lz, hz)
    wx1 = weight(1., ay, ly, hy, az, lz, hz)

    wy0 = weight(0., ax, lx, hx, az, lz, hz)
    wy0_5 = weight(0.5, ax, lx, hx, az, lz, hz)
    wy1 = weight(1., ax, lx, hx, az, lz, hz)

    wz0 = weight(0., ax, lx, hx, ay, ly, hy)
    wz0_5 = weight(0.5, ax, lx, hx, ay, ly, hy)
    wz1 = weight(1., ax, lx, hx, ay, ly, hy)

    sx = (wx0 + 4. * wx0_5 + wx1) * (lx / 6.)

    sy = (wy0 + 4. * wy0_5 + wy1) * (ly / 6.)
    sz = (wz0 + 4. * wz0_5 + wz1) * (lz / 6.)

    return sx, sy, sz


def findlast(x):
    if x.sum() == 0:
        return -1
    else:
        return np.arange(x.size)[x][-1]


def getSourceTermLineCurrentPolygon(xorig, hx, hy, hz, px, py, pz):
    """
        Given a tensor product mesh with origin at (x0,y0,z0) and cell sizes
        hx, hy, hz, compute the source vector for a unit current flowing along
        the polygon with vertices px, py, pz.
        The 3-D arrays sx, sy, sz contain the source terms for all x/y/z-edges
        of the tensor product mesh.

        Modified from matlab code:

            getSourceTermLineCurrentPolygon(x0,y0,z0,hx,hy,hz,px,py,pz)
            Christoph Schwarzbach, February 2014

    """
    import numpy as np
    # number of cells
    nx = len(hx)
    ny = len(hy)
    nz = len(hz)
    x0, y0, z0 = xorig[0], xorig[1], xorig[2]
    # nodal grid
    x = np.r_[x0, x0+np.cumsum(hx)]
    y = np.r_[y0, y0+np.cumsum(hy)]
    z = np.r_[z0, z0+np.cumsum(hz)]

    # discrete edge function
    sx = np.zeros((nx, ny+1, nz+1))
    sy = np.zeros((nx+1, ny, nz+1))
    sz = np.zeros((nx+1, ny+1, nz))

    # number of line segments
    nP = len(px) - 1

    # check that all polygon vertices are inside the mesh
    for ip in range(nP+1):
        ax = px[ip]
        ay = py[ip]
        az = pz[ip]
        ix = findlast(np.logical_and(ax >= x[:nx-1], ax <= x[1:nx]))
        iy = findlast(np.logical_and(ay >= y[:ny-1], ay <= y[1:ny]))
        iz = findlast(np.logical_and(az >= z[:nz-1], az <= z[1:nz]))

        if (ix < 0) or (iy < 0) or (iz < 0):
            msg = "Polygon vertex (%.1f, %.1f, %.1f) is outside the mesh"
            print((msg) % (ax, ay, az))

    # integrate each line segment
    for ip in range(nP):
        # start and end vertices
        ax = px[ip]
        ay = py[ip]
        az = pz[ip]
        bx = px[ip+1]
        by = py[ip+1]
        bz = pz[ip+1]

        # find intersection with mesh planes
        dx = bx - ax
        dy = by - ay
        dz = bz - az
        d = np.sqrt(dx**2+dy**2+dz**2)

        tol = d * np.finfo(float).eps

        if abs(dx) > tol:
            tx = (x - ax) / dx
            tx = tx[np.logical_and(tx >= 0, tx <= 1)]
        else:
            tx = []

        if abs(dy) > tol:
            ty = (y - ay) / dy
            ty = ty[np.logical_and(ty >= 0, ty <= 1)]
        else:
            ty = []

        if abs(dz) > tol:
            tz = (z - az) / dz
            tz = tz[np.logical_and(tz >= 0, tz <= 1)]
        else:
            tz = []

        t = np.unique(np.r_[0., tx, ty, tz, 1.])
        nq = len(t) - 1
        tc = 0.5 * (t[:nq] + t[1:nq+1])

        for iq in range(nq):

            cx = ax + tc[iq] * dx
            cy = ay + tc[iq] * dy
            cz = az + tc[iq] * dz

            # locate cell id

            ix = findlast(np.logical_and(cx >= x[:nx-1], cx <= x[1:nx]))
            iy = findlast(np.logical_and(cy >= y[:ny-1], cy <= y[1:ny]))
            iz = findlast(np.logical_and(cz >= z[:nz-1], cz <= z[1:nz]))

            # local coordinates
            hxloc = hx[ix]
            hyloc = hy[iy]
            hzloc = hz[iz]
            axloc = ax + t[iq]   * dx - x[ix]
            ayloc = ay + t[iq]   * dy - y[iy]
            azloc = az + t[iq]   * dz - z[iz]
            bxloc = ax + t[iq+1] * dx - x[ix]
            byloc = ay + t[iq+1] * dy - y[iy]
            bzloc = az + t[iq+1] * dz - z[iz]
            # integrate
            sxloc, syloc, szloc = getStraightLineCurrentIntegral(hxloc, hyloc,
                                                                 hzloc, axloc,
                                                                 ayloc, azloc,
                                                                 bxloc, byloc,
                                                                 bzloc)
            # integrate
            sx[ix, iy:iy+2, iz:iz+2] += np.reshape(sxloc, (2, 2), order="F")
            sy[ix:ix+2, iy, iz:iz+2] += np.reshape(syloc, (2, 2), order="F")
            sz[ix:ix+2, iy:iy+2, iz] += np.reshape(szloc, (2, 2), order="F")

    return np.r_[Utils.mkvc(sx), Utils.mkvc(sy), Utils.mkvc(sz)]


def getSourceTermLineCurrentPolygon_Octree(mesh, px, py, pz):
    """
        Given a octree mesh with origin at (x0,y0,z0) and cell sizes
        hx, hy, hz, compute the source vector for a unit current flowing along
        the polygon with vertices px, py, pz.
        The 3-D arrays sx, sy, sz contain the source terms for all x/y/z-edges
        of the octree mesh.
    """
    import numpy as np

    # cell widths
    hx = mesh.hx
    hy = mesh.hy
    hz = mesh.hz

    # number of cells
    nx = len(hx)
    ny = len(hy)
    nz = len(hz)

    # mesh origin
    xorig = mesh.x0
    x0, y0, z0 = xorig[0], xorig[1], xorig[2]

    # nodal grid
    x = np.r_[x0, x0+np.cumsum(hx)]
    y = np.r_[y0, y0+np.cumsum(hy)]
    z = np.r_[z0, z0+np.cumsum(hz)]

    # discrete edge vectors
    sx = np.zeros(mesh.nEx)
    sy = np.zeros(mesh.nEy)
    sz = np.zeros(mesh.nEz)

    # number of line segments
    nP = len(px) - 1

    # check that all polygon vertices are inside the mesh
    for ip in range(nP+1):
        ax = px[ip]
        ay = py[ip]
        az = pz[ip]
        ix = findlast(np.logical_and(ax >= x[:nx-1], ax <= x[1:nx]))
        iy = findlast(np.logical_and(ay >= y[:ny-1], ay <= y[1:ny]))
        iz = findlast(np.logical_and(az >= z[:nz-1], az <= z[1:nz]))

        if (ix < 0) or (iy < 0) or (iz < 0):
            msg = "Polygon vertex (%.1f, %.1f, %.1f) is outside the mesh"
            print ((msg) % (ax, ay, az))

    # integrate each line segment
    for ip in range(nP):
        # start and end vertices
        ax = px[ip]
        ay = py[ip]
        az = pz[ip]
        bx = px[ip+1]
        by = py[ip+1]
        bz = pz[ip+1]

        # find intersection with mesh planes
        dx = bx - ax
        dy = by - ay
        dz = bz - az
        d = np.sqrt(dx**2+dy**2+dz**2)

        tol = d * np.finfo(float).eps

        if abs(dx) > tol:
            tx = (x - ax) / dx
            tx = tx[np.logical_and(tx >= 0, tx <= 1)]
        else:
            tx = []

        if abs(dy) > tol:
            ty = (y - ay) / dy
            ty = ty[np.logical_and(ty >= 0, ty <= 1)]
        else:
            ty = []

        if abs(dz) > tol:
            tz = (z - az) / dz
            tz = tz[np.logical_and(tz >= 0, tz <= 1)]
        else:
            tz = []

        t = np.unique(np.r_[0., tx, ty, tz, 1.])
        nq = len(t) - 1
        tc = 0.5 * (t[:nq] + t[1:nq+1])

        for iq in range(nq):

            cx = ax + tc[iq] * dx
            cy = ay + tc[iq] * dy
            cz = az + tc[iq] * dz

            # locate cell id

            ix = findlast(np.logical_and(cx >= x[:nx-1], cx <= x[1:nx]))
            iy = findlast(np.logical_and(cy >= y[:ny-1], cy <= y[1:ny]))
            iz = findlast(np.logical_and(cz >= z[:nz-1], cz <= z[1:nz]))

            # local coordinates
            hxloc = hx[ix]
            hyloc = hy[iy]
            hzloc = hz[iz]
            axloc = ax + t[iq]   * dx - x[ix]
            ayloc = ay + t[iq]   * dy - y[iy]
            azloc = az + t[iq]   * dz - z[iz]
            bxloc = ax + t[iq+1] * dx - x[ix]
            byloc = ay + t[iq+1] * dy - y[iy]
            bzloc = az + t[iq+1] * dz - z[iz]
            # integrate
            sxloc, syloc, szloc = getStraightLineCurrentIntegral(hxloc, hyloc,
                                                                 hzloc, axloc,
                                                                 ayloc, azloc,
                                                                 bxloc, byloc,
                                                                 bzloc)

            # Assign integrated source terms to the proper edges

            # Deal with paths which follow edges
            if(len(np.where(sxloc)[0]) == 1):
                print('Path follows x edge.')
                xEdgeLocs = mesh.gridEx
                d_xEdge = np.sqrt((xEdgeLocs[:,0] - cx)**2 +
                    (xEdgeLocs[:,1] - cy)**2 + (xEdgeLocs[:,2] - cz)**2)

                xEdgeInd = np.argmin(d_xEdge)

                sx[xEdgeInd] += sxloc[0]

            elif(len(np.where(syloc)[0]) == 1):
                print('Path follows y edge.')
                yEdgeLocs = mesh.gridEy
                d_yEdge = np.sqrt((yEdgeLocs[:,0] - cx)**2 +
                    (yEdgeLocs[:,1] - cy)**2 + (yEdgeLocs[:,2] - cz)**2)

                yEdgeInd = np.argmin(d_yEdge)

                sy[yEdgeInd] += syloc[0]

            elif(len(np.where(szloc)[0]) == 1):
                print('Path follows z edge.')
                zEdgeLocs = mesh.gridEz
                d_zEdge = np.sqrt((zEdgeLocs[:,0] - cx)**2 +
                    (zEdgeLocs[:,1] - cy)**2 + (zEdgeLocs[:,2] - cz)**2)

                zEdgeInd = np.argmin(d_zEdge)

                sz[zEdgeInd] += szloc[0]

            # Deal with paths which follow faces
            elif(len(np.where(sxloc)[0]) == 2):
                print('Path follows a y or z face.')
                xEdgeLocs = mesh.gridEx
                d_xEdge = np.sqrt((xEdgeLocs[:,0] - cx)**2 +
                    (xEdgeLocs[:,1] - cy)**2 + (xEdgeLocs[:,2] - cz)**2)

                xEdgeInd = np.argsort(d_xEdge)[0:2]
                sxlocInd = np.argsort(np.abs(sxloc))[2:]

                sx[xEdgeInd[0]] += sxloc[sxlocInd[1]]
                sx[xEdgeInd[1]] += sxloc[sxlocInd[0]]

            elif(len(np.where(syloc)[0]) == 2):
                print('Path follows a x or z face.')
                yEdgeLocs = mesh.gridEy
                d_yEdge = np.sqrt((yEdgeLocs[:,0] - cx)**2 +
                    (yEdgeLocs[:,1] - cy)**2 + (yEdgeLocs[:,2] - cz)**2)

                yEdgeInd = np.argsort(d_yEdge)[0:2]
                sylocInd = np.argsort(np.abs(syloc))[2:]

                sy[yEdgeInd[0]] += syloc[sylocInd[1]]
                sy[yEdgeInd[1]] += syloc[sylocInd[0]]

            elif(len(np.where(szloc)[0]) == 2):
                print('Path follows a x or y face.')
                zEdgeLocs = mesh.gridEz
                d_zEdge = np.sqrt((zEdgeLocs[:,0] - cx)**2 +
                    (zEdgeLocs[:,1] - cy)**2 + (zEdgeLocs[:,2] - cz)**2)

                zEdgeInd = np.argsort(d_zEdge)[0:2]
                szlocInd = np.argsort(np.abs(szloc))[2:]

                sz[zEdgeInd[0]] += szloc[szlocInd[1]]
                sz[zEdgeInd[1]] += szloc[szlocInd[0]]

            # Find edges for paths which do not follow edges or faces
            else:
                cID =  mesh._get_containing_cell_index([cx,cy,cz])
                CC = mesh.gridCC[cID,:]
                CCx = CC[0]
                CCy = CC[1]
                CCz = CC[2]
                # print('CC =', CC)

                xEdgeLocs = mesh.gridEx
                d_xEdge = np.sqrt((xEdgeLocs[:,0] - CCx)**2 +
                    (xEdgeLocs[:,1] - CCy)**2 + (xEdgeLocs[:,2] - CCz)**2)

                xEdgeInd = np.where(d_xEdge < min(mesh.hx))

                yEdgeLocs = mesh.gridEy
                d_yEdge = np.sqrt((yEdgeLocs[:,0] - CCx)**2 +
                    (yEdgeLocs[:,1] - CCy)**2 + (yEdgeLocs[:,2] - CCz)**2)

                yEdgeInd = np.where(d_yEdge < min(mesh.hy))

                zEdgeLocs = mesh.gridEz
                d_zEdge = np.sqrt((zEdgeLocs[:,0] - CCx)**2 +
                    (zEdgeLocs[:,1] - CCy)**2 + (zEdgeLocs[:,2] - CCz)**2)

                zEdgeInd = np.where(d_zEdge < min(mesh.hz))
                # print('(xEdgeInd, yEdgeInd, zEdgeInd) =', xEdgeInd, yEdgeInd,
                #     zEdgeInd)

                # Reorder intergrated source terms to assign them to the right
                # edges
                sx[xEdgeInd] += sxloc[[0, 2, 1, 3]]
                sy[yEdgeInd] += syloc[[0, 2, 1, 3]]
                sz[zEdgeInd] += szloc

    return np.r_[sx, sy, sz]

