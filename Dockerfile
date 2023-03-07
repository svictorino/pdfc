#Download Python from DockerHub and use it
FROM python:3.10.4

#Set the working directory in the Docker container
WORKDIR /code

#Install requirements
RUN apt update
RUN apt install -y ghostscript

#Copy the dependencies file to the working directory
ADD bpdfc.py /code
ADD pdf_compressor.py /code
RUN mkdir /PDFs

## Teste pra ver se o problema de não converter era aqui
## Faltava um chmod mas vai ficar assim
RUN ln -sf /PDFs /code/PDFs 

#Run the container
CMD [ "python", "./bpdfc.py" ]