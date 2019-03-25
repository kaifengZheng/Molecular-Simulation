! A fortran95 program for G95
! By WQY
program rands
    implicit none
    real:: TR, V0
    real:: x2D,y2D,x3D,y3D,z3D, SSQ
    integer:: j,i,N,NPOINTS
    integer:: a,b
    integer,parameter::dims=3
    real,dimension(:,:),allocatable::coords,velocity
    write(*,*) 'give a number of points wanting to sampling NPOINTS:'
    read(*,*) NPOINTS
    write(*,*) 'give a number of substances in the system:'
    read(*,*) N
    write(*,*) 'give TR:'
    read(*,*) TR
    print*,NPOINTS
    print*,N
    allocate(coords(N,dims))
    allocate(velocity(N,dims))
    j = 1
    V0 = sqrt(3.0*TR)
    do i = 1,NPOINTS
        x2D = 2*rand()-1
        y2D = 2*rand()-1
        SSQ = x2D**2+y2D**2
        if(SSQ<=1) then
            x3D = 2.0*x2D*SQRT(1-SSQ)
            y3D = 2.0*Y2D*SQRT(1-SSQ)
            z3D = 1-2.0*SSQ
            coords(i,1)= x3D
            coords(i,2)= y3D
            coords(i,3)= z3D
            velocity(i,1)=v0*x3D
            velocity(i,2)=v0*y3D
            velocity(i,3)=v0*z3D

            j = j+1
            if(J.EQ.N) then
                EXIT
            end if
        end if
    end do
    print "(3f10.2)", velocity
end program
