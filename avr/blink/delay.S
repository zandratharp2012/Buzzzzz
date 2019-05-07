#include "config.h"
    .global      delay
    .section    .text
delay:
        ldi      r26, 255
1:      dec      r26
        brne     1b
        ret

