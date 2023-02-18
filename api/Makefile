build:
	docker build . -f api.dockerfile -t api
run:
	docker run -d --rm -p 8000:8000 --name api api 
run-dev:
	docker run -d --rm -p 8000:8000 -v /home/ionin/PycharmProjects/aas/NeuroHack/api:/api --name api api
stop:
	docker stop api

