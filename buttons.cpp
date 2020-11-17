#include <stdio.h>
#include <wiringPi.h>

// int main(int argc, char** argv)
// {
//     // Intialize the wiringPi Library
//     wiringPiSetup();

// 	const int INPUT_PIN = 12;
	
//     // Read input on this pin
//     pinMode(INPUT_PIN, INPUT);

//     while(true)
//     {
//         // As soon as we dedect an input, log and quit.
//         if(digitalRead(INPUT_PIN) == HIGH)
// 		{
// 			printf("Button is pressed!\n");	
// 			break;
// 		}
//     }

//     // Exit program
//     return 0;
// }

int main()
{
wiringPiSetup();			// Setup the library
pinMode(0, OUTPUT);		// Configure GPIO0 as an output
pinMode(1, INPUT);		// Configure GPIO1 as an input

// Main program loop
while(1)
{
	// Button is pressed if digitalRead returns 0
	if(digitalRead(1) == 1)
{	
	// Toggle the LED
	digitalWrite(0, !digitalRead(0));
delay(500); 	// Delay 500ms
}
}
	return 0;
}
