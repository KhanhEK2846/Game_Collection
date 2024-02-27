#include <iostream>
#include <ctime>
#include <cstring>
using namespace std;

int
main ()
{
  srand (time (NULL));
  int Bullet = rand () % 6 + 1;
  int Hole = 1;
  char Act;

  while (true)
    {
      //cout << Bullet << Hole ;
      cout << "\nShoot (S) or Reload and Shoot (R): ";
      cin >> Act;
      if (Act == 'R' or Act == 'r')
	{
	  Hole = rand () % 6 + 1;
	  Act = 'S';
	}
      if (Act == 'S' or Act == 's')
	{
	  if (Hole == Bullet)
	    {
	      cout << "\nBang! You die, game over!";
	      break;
	    }
	  else
	    {
	      cout << "\nClick";
	      Hole += 1;
	      if (Hole == 7)
		Hole = 1;
	    }
	}



    }


  return 0;
}
