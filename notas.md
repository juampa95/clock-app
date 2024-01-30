Para activar el venv, estando en wsl hay que usar source venv/bin/activate

Para correr la build.sh hay que estar en WSL en el root del proyecto y hacer ./build.sh SIN TENER EL VENV ACTIVO

Eso hace todos los pasos necesarios para dejar la parte estatica de la web en la carpeta public, que es la que se despliega automaticamente en vercel. 

Falta conectar la API que esta en railway con el frontend. Y crear la github actions para que automatice el despliegue. 