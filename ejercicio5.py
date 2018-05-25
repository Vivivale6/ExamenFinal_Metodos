# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 

sigma = 10
beta=2.67
rho=28.0

def funcion1():
    return sigma * (y - x)
def funcion2():
    return rho * x - y -x*z

   
    for (i=0;i<N;i++){

        k1= funcion(x,y);
    
        k2= funcion(x+h/2,y+(h/2.0)*k1);
    
        k3= funcion(x+h/2,y+(h/2.0)*k2);
    
        k4= funcion(x+h/2,y+(h*k3);
                
        y=y+(h/6.0*(k1+2.0*k2+2.0*k3+k4));

        k11= funcion2(x,y,z);
                
        k22= funcion2(x+h/2,y+(h/2.0)*k1,z+(h/2.0)*k1);
                
        k33= funcion2(x+h/2,y+(h/2.0)*k2,z+(h/2.0)*k2);
                
        k44= funcion2(x+h/2,y+(h/2.0)*k3,z+(h*k3);
                  
        z=z+(h/6.0*(k11+2.0*k22+2.0*k33+k44));
    
        x=x+h;











