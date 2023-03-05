//============================================================================
// Name        : optimization_check.cpp
// Author      : Ionut
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <thread>
#include <chrono>
using namespace std;

bool run_thread = true;


void thread_function()
{
	uint32_t counter = 0;
	while( run_thread )
	{
		++ counter;
	}
	std::cout << counter << std::endl;
}

int main() {

	std::thread thr = std::thread( thread_function );
	std::this_thread::sleep_for( std::chrono::milliseconds(1000) );
	run_thread = false;
	thr.join();
	return 0;
}
