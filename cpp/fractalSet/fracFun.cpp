#include <iostream>
#include <iomanip>
#include <complex>
typedef double complex_float;
typedef std::complex<complex_float> complex;

complex xyToComplex(int x, int y, int size) {
  return complex(-1 + complex_float(x)/(size-1), -1 + complex_float(y)/(size-1));;
}

int getIter(const complex& p, int maxIter = 320, const complex& c = complex(-0.5, 0.25)) {
  complex r = p;
  for (int iter = 0; iter < maxIter; ++iter) {
    if (r.real() * r.real() + r.imag() * r.imag() > 4) return iter;
    r = std::pow(r, 2) + c;
  }
  return maxIter;
}

int main() {
  const int size = 500;
  for (int y = 0; y < size; ++y) {
    for (int x = 0; x < size; ++x) {
      int iter = getIter(xyToComplex(x, y, size));
      std::cout << std::setw(3) << iter << ",";
    }
    std::cout << "\n";
  }
  return 0;
}
