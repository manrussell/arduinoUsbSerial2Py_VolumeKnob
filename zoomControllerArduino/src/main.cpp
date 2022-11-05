#include "Arduino.h"

/* reads a potentiometer sensor and sends the reading over serial */

int sensorPin = A0; // the potentiometer is connected to analog pin 0
int ledPin    = 13; // the LED is connected to digital pin 13
int sensorValue;    // an integer variable to store the potentiometer reading

void setup( )
{ 
    pinMode( ledPin, OUTPUT );
    Serial.begin( 9600 );
}

void loop( )
{
    sensorValue = analogRead( sensorPin ); 

    if( sensorValue < 500 )
    {
        digitalWrite( ledPin, LOW ); 
    } 
    else
    {
        digitalWrite( ledPin, HIGH ); 
    }
    delay( 100 ); // Pause in milliseconds

    // wants to be an int
    sensorValue = (int)map( sensorValue,
                       0,
                       1023,
                       -65,
                       0 ); // map to decibels, if expo knob... (-65.25) windows minimum

    Serial.println( sensorValue );
}

// #include "Arduino.h"

// #define LED_BUILTIN_13 ( 13u )

// void flash_helloWorld( void );
// void helloWorld( void );
// void h( void );

// int recvInt = 0;

// void setup( )
// {
//     // pinMode( LED_BUILTIN_13, OUTPUT );
//     // pinMode( A1, INPUT ); // 10-bit adc
//     Serial.begin( 9600 );
//     // Serial.setTimeout( 1 );
//     // while( !Serial.available( ) )
//     //     ;
// }

// int AdcVal = 0;
// void loop( )
// {
//     // while( !Serial.available( ) );

//     // int AdcVal = analogRead( A1 );
//     AdcVal = analogRead( A1 );
//     // ++AdcVal;
//     Serial.println( AdcVal );
//     delay( 50 );

//     // somefiltering/smoothing

//     // h();
//     // helloWorld( );
// }

// void flash_helloWorld( void )
// {
//     // recvInt = Serial.readString( ).toInt( );
//     Serial.println( recvInt++ );
//     Serial.println( "hello world" );
//     digitalWrite( LED_BUILTIN_13, HIGH );
//     delay( 500 );
//     digitalWrite( LED_BUILTIN_13, LOW );
//     delay( 500 );
// }

// void helloWorld( void )
// {
//     Serial.println( recvInt++ );
//     Serial.println( "hello world" );
//     delay( 500 );
// }

// void h( void )
// {
//     Serial.println( recvInt++ );
//     Serial.println( 'h' );
//     delay( 500 );
// }
