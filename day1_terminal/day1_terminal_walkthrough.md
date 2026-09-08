# Day 1: Terminal Basics — Student Reference

> **On Windows?** These commands need a Unix-style shell. Use [WSL (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install) and let the instructor know — everything after this point assumes MacOS or Linux.

---

## Lesson 1: Introduction to the Terminal

The terminal is a text-based window onto the exact same filesystem you already browse with the Finder or a file explorer. Same files, same folders — you type instead of clicking. Nothing you learn today is a separate world.

### 1.1 Opening the Terminal

- **macOS:** press `Cmd + Space`, type `Terminal`, press Enter.
- **Linux:** press `Ctrl + Alt + T`, or search your applications for `Terminal`.
- **Windows** press the `Windows key`, type `powershell`, press Enter. Make sure that you have [WSL installed](https://learn.microsoft.com/en-us/windows/wsl/install).

### 1.2 Reading the Prompt

A typical prompt looks something like:

```
jdoe@MacBook-Pro day1 %
```

Read left to right, the shell is telling you *who* you are (`jdoe`), *what* machine* you are on (`MacBook-Pro`), and *where* you are in the filesystem (`day1`). The final symbol marks where your typing begins.

That final symbol tells you which **shell** you are running. Check it directly:

```bash
echo $SHELL
```

Expected output — one of these:

```
/bin/zsh     # macOS default; prompt ends in %
/bin/bash    # most Linux machines (like CoreHPC) and Windows (with WSL); prompt ends in $
```

Everything in this file works identically in both. If your prompt ends in `$` and your neighbor's ends in `%`, nothing is wrong.

### 1.3 Basic Command Syntax

Nearly every command you will type has the same three-part shape:

```
command  --option  argument
```

- **command** — what to do
- **option** (also called a *flag*) — *how* to do it
- **argument** — *what* to do it to

Type these four in order. They are all the same command with different options:

```bash
ls
ls -l
ls -l -a
ls -la
```

`ls` lists files. `-l` switches to long format (one file per line, with details). `-a` includes hidden files. Notice that `ls -l -a` and `ls -la` do the same thing: **single-dash short flags can be stacked**. Double-dash flags are long names — `ls --all` — and cannot be stacked.

Here is the same shape on a command that does real work (don't run this one yet, just read it):

```bash
cp -r old_folder new_folder
```

`cp` is the command, `-r` is the option, and `old_folder` and `new_folder` are two arguments. **The order of options rarely matters; the order of arguments almost always does.** `cp A B` copies A onto B — the reverse of `cp B A`.

### 1.4 The Two Lifesavers

You will need both of these many times this week.

**Getting help.** Every command ships with a manual page:

```bash
man ls
```

Scroll with the arrow keys or the space bar, search by typing `/` followed by a word, and **press `q` to quit**.

**Getting out.** Sometimes commands will break and you will need to cancel them. Type this deliberately broken command — an opening quote with no closing quote — and press Enter:

```bash
ls -l "
```

The shell will hang, waiting for you to close the quote. To escape, press:

```
Ctrl + c
```

You are back at a prompt. **`Ctrl + c` is your emergency exit** for anything that is running when you want it to stop.

### 1.5 Typing Faster

The mouse does not move your cursor in the terminal. Use these instead:

| Keys | Effect |
| --- | --- |
| Up arrow | Recall the previous command (press repeatedly for older ones) |
| `Ctrl + a` | Jump to the start of the line |
| `Ctrl + e` | Jump to the end of the line |
| `clear` (or `Cmd + K`) | Clear the screen |

---

## Lesson 2: Navigating the File System

### 2.1 pwd — Print Working Directory

The terminal is always "in" exactly one directory at a time. To ask which:

```bash
pwd
```

Expected output, something like:

```
/Users/jdoe          # macOS
/home/jdoe           # Linux
```

That is your **home directory** — the top of your personal space on this machine. macOS puts homes under `/Users`, Linux under `/home`. Same idea, different name.

**When you are confused about anything today, the first move is always `pwd`, then `ls`.** You may also find it useful to use `open .` (macOS), `xdg-open .` (Linux), or `explorer.exe .` (Windows) to open a Finder/Explorer window on the current directory.

### 2.2 ls — List

```bash
ls
ls -l
ls -lh
ls -a
ls -lt
```

What each flag gives you:

- `-l` — **long** format. The columns are: permissions, number of links, owner, group, size in bytes, last-modified date, name. We come back to that first permissions column in Lesson 6.
- `-h` — **human-readable** sizes, so `4096` becomes `4.0K`. Only does something when combined with `-l`.
- `-a` — **all** files, including hidden ones. Files whose names start with `.` are hidden by convention, not by magic. Note that `.` and `..` show up here — they are real entries, and we use both in a moment. If you are on a Mac, you are probably seeing your first-ever `.DS_Store`.
- `-t` — sort by **time**, newest first. Add `-r` to reverse it. This is the flag you will actually reach for daily once you have real data.

### 2.3 cd — Change Directory

```bash
cd ~
pwd
cd Documents
pwd
cd ..
pwd
cd -
pwd
cd
pwd
```

Watch the `pwd` output after each step. The special names:

| Name | Means |
| --- | --- |
| `~` | Your home directory |
| `..` | The parent directory (one level up) |
| `.` | The current directory (useful for referring to the current directory explicitly) |
| `-` | The directory you were in just before this one |
| *(nothing)* | `cd` with no argument goes home (same as `cd ~`) |

### 2.4 Tab Completion

Make sure you are in your home directory, then type `cd Doc` — do **not** press Enter — and press the **Tab** key. The shell finishes the word for you:

```bash
cd Doc<Tab>        # becomes: cd Documents/
```

Now press `Ctrl + c` to abandon that line, type `cd D`, and press Tab . The shell lists every directory starting with `D`, because it cannot tell which one you meant.

**Tab is a spell-checker for filenames.** If Tab refuses to complete, what you are typing does not exist — you are in the wrong directory, or you have a typo. Trust Tab over your own typing.

### 2.5 mkdir — Make Directory

Let's build the folder you will work in for the rest of the course:

```bash
cd
mkdir -p intro_to_programming/day1/analysis/round1/plots
cd intro_to_programming/day1
pwd
```

Expected output from `pwd`:

```
/Users/jdoe/intro_to_programming/day1
```

**Why `-p`?** Plain `mkdir intro_to_programming/day1/analysis/round1/plots` fails if any of the folders in the path do not exist — it will not create a chain. `-p` creates every missing level, and it does not complain if the directory is already there.

### 2.6 Relative vs Absolute Paths

There are two ways to reference any file or directory:

- A **relative path** is directions from where you are standing right now (your current directory).
- An **absolute path** starts with `/` and is unambiguous from anywhere on the
  machine (the exact path to your directory of interest).

Make sure you are in your day1 directory, then try all four of these — they all name the same folder:

```bash
cd ~/intro_to_programming/day1
ls analysis                                  # relative: "analysis, starting from here"
ls ./analysis                                # identical — the ./ is explicit but optional
ls ~/intro_to_programming/day1/analysis      # ~ expands to your home directory
ls /Users/jdoe/intro_to_programming/day1/analysis    # absolute
```

**On that last line, substitute your own home directory** — run `pwd` and use what it prints. `/Users/jdoe` is an example, not your path.

Now prove to yourself that the difference is real. Move to the root of the filesystem (the root - `/` - not your home directory) and try both kinds of path:

```bash
cd /
ls analysis                                          # fails: "No such file or directory"
ls /Users/jdoe/intro_to_programming/day1/analysis    # works
cd ~/intro_to_programming/day1
```

The relative path broke because there is no `analysis` folder at `/`. The absolute path worked because it did not depend on where you were.

**Which to use:** relative paths while you are working interactively; absolute paths are safer for scripts and job submissions.

---

## Lesson 3: File Operations

```bash
cd ~/intro_to_programming/day1
```

### 3.1 touch — Create an Empty File

```bash
touch notes.txt
ls -l notes.txt
```

Note the size column: `0`. The file exists and is empty.

### 3.2 Putting Something in the File

Run this so you have something to read in the next section:

```bash
printf 'line one\nline two\nline three\nline four\nline five\n' > notes.txt
```

Don't worry about how it works just yet, we'll go over this later. For now, know that it sent the output into the file instead of onto your screen.

### 3.3 cat, head, tail — Viewing Files

```bash
cat notes.txt
head notes.txt
tail notes.txt
head -n 2 notes.txt
tail -n 1 notes.txt
```

- `cat` dumps the **entire** file to the screen. This is fine for small files.
- `head` shows the **first** lines, `tail` the **last**. Both default to 10.
- `-n` sets how many lines. `head -n 2 notes.txt` means "two lines," not "two files."
- For anything long, `less notes.txt` is the humane option — same navigation as `man`, and `q` to quit.

### 3.4 cp, mv, rm — Copy, Move, Delete

Run these one at a time and read the `ls` output after each step:

```bash
cp notes.txt notes_backup.txt
ls

mv notes_backup.txt notes_old.txt      # same directory = rename
ls

mkdir archive
mv notes_old.txt archive/              # different directory = move
ls
ls archive

cp -r archive archive_copy             # -r is required for directories
ls

rm -r archive_copy
ls
```

Two things to note:

- **`mv` is both "move" and "rename."** There is no separate rename command, because renaming *is* moving a file within its own directory.
- **`cp` and `rm` need `-r` (recursive) for directories.** Without it you get "omitting directory" or "is a directory."

---

## Lesson 4: Text Editing

### 4.1 nano (my default)

nano's great virtue is that it tells you what to press: the shortcuts are printed at the bottom of the screen.

```bash
cd ~/intro_to_programming/day1
nano hello.txt
```

Now:

1. **Just type.** Type your name and a sentence to see how it works.
2. Arrow keys move the cursor; `Ctrl + a` and `Ctrl + e` jump to the start and end of a line.
3. Press `Ctrl + S` to save
4. Press `Ctrl + X` to exit. If you have unsaved changes it asks Y/N first.

Look at the two-line menu at the bottom before you leave. It shows things like `^X Exit`. **`^` means Ctrl** — so `^X` is telling you to press `Ctrl + x`.

Note that **`Ctrl + C` inside nano does not quit.** It shows your cursor position.

Prove your file saved:

```bash
cat hello.txt
```

### 4.2 vim (another popular option)

You will meet vim whether or not you choose to. `git` and several other tools open it by default, and if you don't know how to leave, you are genuinely stuck.

```bash
vim scratch.txt
```

Follow along carefully — vim gives you almost no visual feedback:

1. You start in **normal mode**. Keys here are *commands*, not text. Pressing `dd` deletes a line; it does not type the letters "dd".
2. Press `i` for **insert mode**. Look for `-- INSERT --` at the bottom of the screen. Now type: `hello from vim`.
3. Press `ESC` to return to normal mode. The `-- INSERT --` indicator disappears.
4. Type `:w` and press Enter — **write** (save).
5. Type `:q` and press Enter — **quit**.

The commands worth memorizing:

| Command | Effect |
| --- | --- |
| `i` | Enter insert mode (type text) |
| `ESC` | Return to normal mode |
| `:w` | Save |
| `:q` | Quit |
| `:wq` | Save and quit |
| `:q!` | Quit, throwing away changes |

**`ESC` then `:q!` is the universal escape hatch.** If you ever find yourself stuck in vim, this will get you out.

---

## Lesson 5: Piping and Redirection

Every command reads from an input and writes to an output. By default, output is your screen. Pipes and redirects re-aim it. This can allow you to chain together many simple commands into something more powerful.

```
command1  |  command2      # output of command1 becomes the input of command2
command   >  file          # output goes into file, overwriting it
command   >> file          # output is appended to the end of file
```

### 5.1 Set Up Some Files Worth Filtering

```bash
cd ~/intro_to_programming/day1
mkdir -p pipes
cd pipes
touch a.txt b.txt c.txt structure1.pdb structure2.pdb structure3.pdb readme.md
ls
```

Expected output:

```
a.txt  b.txt  c.txt  readme.md  structure1.pdb  structure2.pdb  structure3.pdb
```

### 5.2 Piping with `|`

Build this up one stage at a time, running each line, so you can watch the stream get narrower:

```bash
ls
ls | wc -l
ls | grep "pdb"
ls | grep "pdb" | wc -l
```

- `wc -l` counts **lines**. When `ls` is piped into another command it prints one name per line, so this counts your files.
- `grep "pattern"` keeps only the lines that contain the pattern.
- Pipes chain as long as you like. Each `|` hands the previous command's output to the next one.

Pipes work on file *contents*, not just filenames. The following counts how many lines in `notes.txt` contain the word "line":

```bash
cat ../notes.txt | grep "line" | wc -l
```

### 5.3 Redirection with `>` and `>>`

```bash
ls *.pdb > pdb_list.txt
cat pdb_list.txt
```

You now have a file containing a list of your `.pdb` files. Notice the `ls` output never appeared on screen — it went into the file instead.

Now the difference between the two arrows:

```bash
echo "first" > log2.txt
cat log2.txt
echo "second" > log2.txt
cat log2.txt
```

"first" is **gone**. `>` overwrites the target file's existing contents. Alternatively, `>>` appends to the end of the file:

```bash
echo "# analysis notes" > log.txt
echo "ran step 1" >> log.txt
echo "ran step 2" >> log.txt
cat log.txt
```

Expected output:

```
# analysis notes
ran step 1
ran step 2
```

### 5.4 The `*` Wildcard

`*.pdb` means "anything ending in `.pdb`". The important part is *who* expands it —
the **shell** does, before the command ever sees it. Prove it:

```bash
echo *.pdb
```

Expected output:

```
structure1.pdb structure2.pdb structure3.pdb
```

`echo` knows nothing about files; it just printed the arguments it was handed. In this case, the arguments were all files ending in `.pdb`.

---

## Lesson 6: Scripting Basics

### 6.1 Write the Script

```bash
cd ~/intro_to_programming/day1
nano hello.sh
```

Type this in (save with `Ctrl + S`, Enter, then exit with `Ctrl + X`):

```bash
#!/bin/bash

# A first script: report where we are and what is here.
echo "Hello, world!"
echo "You are here:"
pwd
echo "This directory contains:"
ls
echo "Done."
```

Line by line:

- `#!/bin/bash` is the **shebang**. It tells the system which program should interpret this file. It must be the very first line, with no blank line above it.
- `#` starts a **comment** — a note for humans that the shell ignores.
- Every other line is a simple command - just like the others you've already used today.

### 6.2 Make It Executable

```bash
ls -l hello.sh
chmod +x hello.sh
ls -l hello.sh
```

The first and second `ls` calls should show something like this in the permissions column:

```
-rw-r--r--    →    -rwxr-xr-x
```

That new `x` is the "may be executed" permission bit tha twas added by running `chmod +x hello.sh`. Without the `x`, the shell will refuse to run your file.

(On macOS you may see a trailing `@`, like `-rwxr-xr-x@`. That just means the file carries some extended attributes. Ignore it.)

### 6.3 Run It

First, do it wrong. Attempt to run your script by typing its name:

```bash
hello.sh
```

Now do it right:

```bash
./hello.sh
```

When you type a bare command name, the shell searches a specific list of directories called your `PATH` — and for security reasons the current directory is deliberately *not* on that list. `./` means "right here, in this directory," and allows you to run your script.

There is a second way that skips `chmod` entirely:

```bash
bash hello.sh
```

Here you are running `bash` and handing it your file as an argument, so the executable bit never comes into it. Both are correct and you can use what you prefer.

---

## Final Note:

Now you know enough to navigate the terminal, use commands, and write a simple script. Today, we did all of this **locally** on our personal machines. However, these skills are exactly what you would use on a remote server (like CoreHPC), and might be very useful for your own research.

---

## Command Reference

| Command | What it does |
| --- | --- |
| `pwd` | Print the current directory |
| `ls` | List files (`-l` long, `-a` all, `-h` human sizes, `-t` by time) |
| `cd` | Change directory (`~` home, `..` up, `-` previous, bare = home) |
| `mkdir -p` | Create directories, including missing parents |
| `touch` | Create an empty file / update a timestamp |
| `cat` | Print an entire file |
| `head -n N` | Print the first N lines |
| `tail -n N` | Print the last N lines |
| `less` | Page through a long file (`q` to quit) |
| `cp` | Copy (`-r` for directories, `-i` to prompt) |
| `mv` | Move **or** rename |
| `rm` | Delete permanently (`-r` for directories, `-i` to prompt) |
| `nano` | Terminal editor (`Ctrl + O` save, `Ctrl + X` exit) |
| `vim` | Terminal editor (`i` insert, `ESC`, `:wq` save+quit, `:q!` force quit) |
| `echo` | Print text |
| `grep` | Keep only matching lines (`-c` to count them) |
| `wc -l` | Count lines |
| `readlink -f` | Print a file's absolute path |
| `chmod +x` | Make a file executable |
| `man` | Read a command's manual (`q` to quit) |
| `clear` | Clear the screen |

| Symbol | Meaning |
| --- | --- |
| `\|` | Pipe: send output to another **command** |
| `>` | Redirect: send output into a **file**, overwriting it |
| `>>` | Redirect: **append** output to the end of a file |
| `*` | Wildcard, expanded by the shell before the command runs |
| `#` | Comment (ignored) |
| `#!/bin/bash` | Shebang: which interpreter runs this script |
| `$1` | The first argument passed to a script |
| `Ctrl + c` | Cancel whatever is running |
| `Tab` | Complete a filename |

---

## Before Next Class

- Install [VSCode](https://code.visualstudio.com) if you don't have it already.
- Sign up for a [GitHub](https://github.com) account, and then for the free
  [GitHub Student Developer Pack](https://education.github.com/pack).
