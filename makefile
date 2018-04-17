PDE.pdf: resultados.txt grafica.py
	python grafica.py
resultados.txt: adveccion.cpp
	c++ adveccion.cpp
	./a.out > resultados.txt
	rm a.out
