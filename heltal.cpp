#include <cstdlib>

// Integer class 
class Heltal{
	public:
		Heltal(int);
		int get();
		void set(int);
		long long fib();
	private:
		long long _fib(int);
		int val;
	};
 
Heltal::Heltal(int n){
	val = n;
	}
 
int Heltal::get(){
	return val;
	}
 
void Heltal::set(int n){
	val = n;
	}
long long Heltal::fib(){
	long long ret =  Heltal::_fib(val);
	return ret;
}
long long Heltal::_fib(int n){
	if(n<=1) {
      return((long long) n);
   }else {
      return(Heltal::_fib(n-1)+Heltal::_fib(n-2));
   }
}



extern "C"{
	Heltal* Heltal_new(int n) {return new Heltal(n);}
	int Heltal_get(Heltal* heltal) {return heltal->get();}
	long long Heltal_fib(Heltal* heltal) {return heltal->fib();}
	void Heltal_set(Heltal* heltal, int n) {heltal->set(n);}
	void Heltal_delete(Heltal* heltal){
		if (heltal){
			delete heltal;
			heltal = nullptr;
			}
		}
	}