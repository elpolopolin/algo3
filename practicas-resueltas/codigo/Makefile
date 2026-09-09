CXX      ?= g++
CXXFLAGS ?= -std=c++17 -O2 -Wall -Wextra

# Cada .cpp con main() es un ejecutable de test.
SRCS := $(wildcard p*.cpp)
BINS := $(SRCS:.cpp=)

.PHONY: all test clean
all: $(BINS)

# make p1_pascal  -> compila y lo corre
$(BINS): %: %.cpp comun.h
	$(CXX) $(CXXFLAGS) -o $@ $< $(EXTRA_$@)
	./$@

# grafo.cpp se linkea con los ejercicios de la práctica 3
EXTRA_p3_triangulos := grafo.cpp

test: $(SRCS)
	@set -e; for s in $(SRCS); do \
	  b=$${s%.cpp}; \
	  echo "== $$b =="; \
	  $(CXX) $(CXXFLAGS) -o $$b $$s $(EXTRA_$$b) 2>/dev/null || $(CXX) $(CXXFLAGS) -o $$b $$s; \
	  ./$$b; \
	done

clean:
	rm -f $(BINS) *.o
