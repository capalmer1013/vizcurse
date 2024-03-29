#include <sys/ioctl.h>
#include <stdio.h>
#include <unistd.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

#ifndef M_PI
#    define M_PI 3.14159265358979323846
#endif

const char* MOVE_CURSOR_TOP_LEFT = "\033[%dA";  // format with number of lines to move
const char* BACKGROUND = "\033[48;2;%d;%d;%dm"; // format with R, G, B  (24 bit RGB)
const char* FOREGROUND = "\033[38;2;%d;%d;%dm"; // format with R, G, B  (24 bit RGB)

int scaled_sin(int x, int scale) {
    double radians = x * (M_PI / 180.0); // Convert the integer to radians
    double sine_value = sin(radians); // Calculate the sine of the angle in radians

    // Scale the sine value to be between 0 and scale, and then cast it to an int
    int scaled_value = (int)((sine_value + 1) * scale);

    return scaled_value;
}

void set_color(int x, int y, int t) {
    t *= 4;
    printf(
        BACKGROUND,
        abs(y-scaled_sin(t, 256)        ) % 256,  // R
        abs((x-scaled_sin(t, 256)) * y  ) % 256,  // G
        abs(x * y + t                   ) % 256   // B
    );
}

int main() {
    struct winsize w;
    ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
    int x, y, t = 0;
    int width   = w.ws_col;
    int height  = w.ws_row;

    while (1) {
        for (y = 0; y < height; y++) {
            for (x = 0; x < width; x++) {
                set_color(x, y, t);
                putchar(' ');
            }
            putchar('\n');
        }
        fflush(stdout);
        t++;
        usleep(33333); // Sleep for 1/30 second
        printf(MOVE_CURSOR_TOP_LEFT, height);
    }

    return 0;
}