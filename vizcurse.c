#include <stdio.h>
#include <unistd.h>
#include <time.h>

void set_color(int x, int y, int t) {
    // Set the foreground color using ANSI escape codes with 24-bit RGB format
    printf("\033[38;2;%d;%d;%dm", x % 256, y % 256, t % 256);
}

int main() {
    int x, y, t = 0;
    int width = 80;   // Console width
    int height = 25;  // Console height

    while (1) {
        for (y = 0; y < height; y++) {
            for (x = 0; x < width; x++) {
                set_color(x, y, t);
                putchar('#');
            }
            putchar('\n');
        }
        fflush(stdout);

        t++; // Increment time (count of complete for loop iterations)
        usleep(10000); // Add some delay (in microseconds) between frames

        // Reset the console cursor position to the top-left corner
        printf("\033[%dA", height);
    }

    return 0;
}