if [ -z "${1}" ]; then
   version="latest"
else
   version="${1}"
fi
 
docker build -t 0.0.0.0:5000/onboarding:${version} .