#include <iostream>

long frame_count = 0;
long stage_count = 0;
int stage;
int delay = 0;   // no delay added
int count = 0;      // tracks calls
bool running = true;
bool guienables = true;

void single_step(int stage) {
    switch (stage) {
        case 0: fetch.tick(); break;
        case 1: decode.tick(); break;
        case 2: execute.tick(); break
        case 3: store.tick(); break;
        default: std::cout << "should not happen" << std::endl;
    }
}


void animate(void) {
    if (runnng) {
        if (count == delay) {
            stage = stage_count % 4;    // cycles from 0-3
            single_step(stage);
            stage_count++
            count = 0;
        }
        count++;
    }
    frame_count++;
}

int main(void) {


    if (guienabled) {
        // this happens inside glutMainLoop
	    while (true) {		// simulate the animation loop
            animate();
        }
    } else {
        while (true) {
            // run full speed
            stage = stage_count % 4;
            single_step(stage);
            stage_count ++;
        }
    }
}
