# CS571-hw1
To test the program 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install docker.

First is to check the existing network. Go to terminal and type:

`
docker network ls
`

To create the network:

`
docker network create converters
`

To create the images:

`
docker image build -t city_converter city_converter
`

`
docker image build -t zip_converter zip_converter
`

In order to containerize the images of python code, run the following commands:

`
docker run -d --rm --net converters -p 8888:8888 --name city_converter city_converter
`

`
docker run -d --rm --net converters -p 8000:8000 --name zip_converter zip_converter
`

The next step is to open browser and go to http://localhost:8888/zipcode?city=New%20York

The browser should look like this:

<img width="736" alt="Screen Shot 2023-02-10 at 7 40 41 AM" src="https://user-images.githubusercontent.com/123494938/217968330-8f735817-03fe-469a-a197-1d7b92b0a879.png">

You can also try Los Angeles and Chicago to see the different results.
