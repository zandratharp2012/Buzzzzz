#include <avr/io.h>

#define LED_PIN     5
#define LED_PORT    _(PORTB)
#define LED_DIR     _(DDRB)

// include this line to avoid SFR_REG issues
#define _(s)    _SFR_IO_ADDR(s)
