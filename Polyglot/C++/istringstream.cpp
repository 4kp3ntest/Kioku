// istringstream::str
#include <string>       // std::string
#include <vector>       // std::vector
#include <iostream>     // std::cout
#include <sstream>      // std::istringstream
#include <iterator>     // std::istream_iterator

int main () {
  std::istringstream iss;
  std::string strvalues = "32 240 2 1450";

  iss.str (strvalues);

  for (int n=0; n<4; n++)
  {
    int val;
    iss >> val;
    std::cout << val << '\n';
  }

  std::cout << "Finished writing the numbers in: ";
  std::cout << iss.str() << '\n';

  std::vector<std::string> results((std::istream_iterator<std::string>(iss)),
                            std::istream_iterator<std::string>());
  /*Produces Segfault*/
  std::cout << results[0];
  return 0;
}
