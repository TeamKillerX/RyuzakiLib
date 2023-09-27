// hack developer by @xtdevs
// you need learn to c++

#include <iostream>
#include <string>

class PrivateApiUrl {
public:
    PrivateApiUrl(
        std::string url = "private.randydev.my.id",
        std::string method = nullptr,
        std::string punctuation = "?",
        std::string parameter = nullptr,
        std::string allow_web = "https"
    ) {
        this->url = url;
        this->method = method;
        this->punctuation = punctuation;
        this->parameter = parameter;
        this->allow_web = allow_web;
    }
    std::string checking() {
        std::string api_url = this->allow_web + "://" + this->url + "/" + this->method + this->punctuation + this->parameter;
        return api_url;
    }
private:
    std::string url;
    std::string method;
    std::string punctuation;
    std::string parameter;
    std::string allow_web;
};

int main() {
    PrivateApiUrl obj;
    std::string result = obj.checking();
    std::cout << result << std::endl;
    return 0;
}
