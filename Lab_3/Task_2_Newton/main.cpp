#include <iostream>
#include <cmath>

//const double e = exp(1.0);

double function(double x) {
	return exp(-(x * x)) - pow((x - 1), 2);
}

double diff_function(double x) {
	return -2 * x * (exp(-(x * x))) - 2 * x + 2;
}

double newton(double(*f)(double), double(*df)(double), double x0, double eps) {
	double x = 0;
	double delta = 1;

	while (delta > eps) {
		x = x0 - (f(x0) / df(x0));
		delta = abs(x - x0);
		x0 = x;
	}

	return x;

}


int main() {
	double eps = pow(10, -4);
	double x0 = 0;

	std::cin >> x0;

	std::cout << std::fixed << newton(function, diff_function, x0, eps) << std::endl;
	return 0;
}