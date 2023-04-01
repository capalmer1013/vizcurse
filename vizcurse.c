#include <stdio.h>
#include <unistd.h>
#include <math.h>
#include <time.h>

#ifndef M_PI
#    define M_PI 3.14159265358979323846
#endif

int scaled_sin(int x) {
    double radians = x * (M_PI / 180.0); // Convert the integer to radians
    double sine_value = sin(radians); // Calculate the sine of the angle in radians

    // Scale the sine value to be between 0 and 256, and then cast it to an int
    int scaled_value = (int)((sine_value + 1) * 128);

    return scaled_value;
}

void set_color(int x, int y, int t) {
    // Set the foreground color using ANSI escape codes with 24-bit RGB format
    printf(
        "\033[38;2;%d;%d;%dm",
        scaled_sin(x)  % 256,
        scaled_sin(y)  % 256,
        scaled_sin(t)  % 256
    );
}

int main() {
    int x, y, t = 0;
    int width   = 200;   // Console width
    int height  = 50;    // Console height

    while (1) {
        for (y = 0; y < height; y++) {
            for (x = 0; x < width; x++) {
                set_color(x, y, t);
                putchar('#');
            }
            putchar('\n');
        }
        fflush(stdout);

        t++;            // Increment time (count of complete for loop iterations)
        usleep(10000);  // Add some delay (in microseconds) between frames

        // Reset the console cursor position to the top-left corner
        printf("\033[%dA", height);
    }

    return 0;
}