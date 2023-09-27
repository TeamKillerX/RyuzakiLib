// part 1

#include <iostream>
#include <string>

using namespace std;

int main() {
    string url = "private.randydev.my.id";
    string method = "mediafire";
    string punctuation = "?";
    string parameter = "link=value";
    string allow_web = "https";

    cout << allow_web + "://" + url + "/" + method + punctuation + parameter;

    return 0;
}
