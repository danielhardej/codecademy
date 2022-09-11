## Quiz: Redirecting Input and Output

#### Append the string “Aesop Rock” to the file greatest.txt

- [ ] cat "Aesop Rock" >> greatest.txt
- [ ] cat "Aesop Rock" > greatest.txt
- [x] echo "Aesop Rock" >> greatest.txt
- [ ] None of these

#### What does the < symbol do?

- [x] Redirect input to a command
- [ ] Output commands
- [ ] It both redirects input to a command and outputs commands
- [ ] Append command to file

#### Search the file greatest.txt for “Earl”, then send the results to the file oddfuture.txt.

- [x] grep "Earl" greatest.txt >> oddfuture.txt
- [ ] grep "Earl" greatest.txt | oddfuture.txt
- [ ] grep "Earl" greatest.txt cat oddfuture.txt
- [ ] grep "Earl" oddfuture.txt

#### The uniq command removes duplicates ____

- [ ] If they are separated
- [x] Only if they are adjacent
- [ ] None of these
- [ ] From the entire input

#### What command searches all files recursively for “Gambino”?

- [ ] grep "Gambino"
- [ ] grep Gambino | *
- [ ] grep -a "Gambino"
- [x] grep -R "Gambino" .

#### The echo command takes a string as ____ and prints that string as ____

- [ ] stderr, stdout
- [x] stdin, stdout
- [ ] stdin, stderr
- [ ] stdout, stdin

#### What does the s stand for in the 's/Hopsin/Kanye' part of sed 's/Hopsin/Kanye'?

- [ ] Stringent
- [x] Substitute
- [ ] Search
- [ ] Secondary

#### How would you pipe the results of one command to another?

- [x] command | command
- [ ] command > command
- [ ] command >> command
- [ ] command < command

#### What commands would sort the contents of the file greatest.txt and print them?

- [x] cat greatest.txt | sort
- [ ] cat greatest.txt >> sort
- [ ] echo greatest.txt > sort
- [ ] None of these

#### What command outputs the string “Lamar” to the file greatest.txt?

- [ ] mv "Lamar" greatest.txt
- [ ] cat "Lamar" greatest.txt
- [x] echo "Lamar" > greatest.txt
- [ ] echo "Lamar" < greatest.txt
