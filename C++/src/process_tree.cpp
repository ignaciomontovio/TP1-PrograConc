#include <cstring>
#include <iostream>
#include <map>
#include <sstream>
#include <sys/wait.h>
#include <unistd.h>
#include <vector>

using namespace std;

struct Node
{
  char letter;
  pid_t pid;
  pid_t parent;

  Node(char letter_)
  {
    letter = letter_;
    pid = getpid();
    parent = getppid();
  }

  std::string toString()
  {
    std::stringstream aux;
    aux << "Process: " << letter << ", PID: " << pid << ", Parent PID: " << parent;
    return aux.str();
  }
};
typedef struct Node Node;

int main(int argc, char *argv[])
{
  map<char, vector<char>> nodes_map =
  {
    {'A', {'B', 'C'}},
    {'B', {'D', 'E'}},
    {'C', {'F'}},
    {'E', {'G', 'H'}},
  };

  Node current = Node('A');
  cout << current.toString() << endl;

  vector<char>::iterator next_child = nodes_map[current.letter].begin();
  vector<char>::iterator end = nodes_map[current.letter].end();

  while (next_child != end)
  {
    pid_t new_child = fork();

    if (new_child < 0)
    {
      cerr << "Error: " << strerror(errno) << endl;
      return EXIT_FAILURE;
    }

    if (new_child == 0)
    {
      current = Node(*next_child);
      cout << current.toString() << endl;

      // Si el hijo tiene que crear mas nodos reiniciamos el iterador.
      if (nodes_map.find(current.letter) != nodes_map.end())
      {
        next_child = nodes_map[current.letter].begin();
        end = nodes_map[current.letter].end();
        continue;
      }

      break; // Sino terminamos el loop.
    }

    next_child++;
  }

  if (nodes_map.find(current.letter) != nodes_map.end())
  {
    next_child = nodes_map[current.letter].begin();
    for (; next_child != end; next_child++)
    {
      wait(NULL);
    }
  }
  else
  {
    unsigned int time = 10;

    if (argc > 1)
    {
      try
      {
        time = stoi(argv[1]);
      }
      catch(const invalid_argument& e)
      {
        cerr << "Invalid time passed as parameter, using default time (" << time << " seconds)." << endl;
      }
    }

    sleep(time);
  }

  cout << "Cerrando proceso: " << current.letter << endl;

  return EXIT_SUCCESS;
}