#include <iostream>
#include <cmath>
#include <string>

struct section {
	double a;
	double b;
};

double function(double x) {
	return exp(-(x * x)) - pow((x - 1), 2);
}

double dichot(double(*f)(double), double a, double b, double eps) {
	section sect = { a, b };
	double c;

	while (fabs(sect.b - sect.a) > eps) {
		c = (sect.a + sect.b) / 2;
		
		if (f(a) * f(c) < 0) {
			sect.b = c;
		}
		else if (f(b) * f(c) < 0) {
			sect.a = c;
		}
		else {
			std::cout << "Error";
			return c;
		}


	}

	return c;
}

//double roundoff(double x, int n) {
//	std::string s = "1";
//	for (int i = 0; i < n; i++) {
//		s += '0';
//	}
//	n = std::stoi(s);
//	return round(x * n) / n;
//}


int main() {
	(std::cout).precision(20);
	double a, b;
	double eps = pow(10, -4);

	std::cin >> a;
	std::cin >> b;

	std::cout << std::fixed << dichot(function, a, b, eps);
	return 0;
}