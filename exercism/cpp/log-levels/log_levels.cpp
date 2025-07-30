#include <string>

namespace log_line {
std::string message(std::string line) {
    int i = line.find(":") + 2;
    return line.substr(i, line.length() - i);
}

std::string log_level(std::string line) {
    int i = line.find(":") - 2;
    return line.substr(1, i);
}

std::string reformat(std::string line) {
    std::string level = log_level(line);
    std::string log_message = message(line);

    return log_message + " (" + level + ")";
}
}  // namespace log_line
