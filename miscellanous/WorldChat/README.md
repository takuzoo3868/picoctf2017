<!-- This markdown file is writeup template. -->

## WorldChat 30pt

### Problem
> We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:38798. Remember to use Ctrl-C to cut the connection if it overwhelms you!

### Answer
Accessing the specified port, Chat is started.

```bash
$ nc shell2017.picoctf.com 38798
worldchat v2.3002.4
setting up readonly client...done
connecting to feed..done
Welcome to WORLDCHAT!

19:24:12 nikia: Several heavily mustached dolphins want to see me to drink your milkshake
19:24:12 clinton: We need to meet up for the future of humanity
19:24:12 hildegard: Scary pandas , in my opinion, are our best chance for the future of humanity
19:24:12 janett: my homegirlz will never be able to create a self driving car
19:24:12 kelvin: I wants to see me for what, I do not know
19:24:12 patience: We want to see me to drink your milkshake
19:24:12 christene: that guy from that movie gives me hope for the future of humanity
19:24:12 jazmin: Scary pandas are the best of friends to create a self driving car
19:24:12 noihazflag: my homegirlz , in my opinion, are our best chance for the future of humanity
19:24:12 leandro: Several heavily mustached dolphins want to see me to generate fusion power
19:24:12 diana: A huge moose wants to see me for the future of humanity
19:24:13 dede: My friend would like to meet you for the future of humanity
19:24:13 gregg: your dad would like to meet you to make a rasberry pie
19:24:13 sheilah: I gives me hope for the future of humanity
19:24:13 noihazflag: A dog with a cape wants to steal my sloth to help me spell 'raspberry' correctly
19:24:13 whatisflag: My friend gives me hope to make a rasberry pie
19:24:13 sonny: my homegirlz will never be able for the future of humanity
19:24:13 flagperson: this is part 1/8 of the flag - 3572
19:24:13 jazmin: Hungry jackolanterns need to meet up to help me spell 'raspberry' correctly
```
The person named `flagperson` is writing flag information. Let's extract posts.

```bash
$ nc shell2017.picoctf.com 38798 | grep flagperson
19:25:44 flagperson: this is part 1/8 of the flag - 3572
19:25:46 flagperson: this is part 2/8 of the flag - dd03
19:25:49 flagperson: this is part 3/8 of the flag - 4e91
19:25:50 flagperson: this is part 4/8 of the flag - 5f49
19:25:54 flagperson: this is part 5/8 of the flag - 3120
19:25:57 flagperson: this is part 6/8 of the flag - 885d
19:26:00 flagperson: this is part 7/8 of the flag - 41d5
19:26:00 flagperson: this is part 8/8 of the flag - 46c7
19:26:03 flagperson: this is part 1/8 of the flag - 3572
```

### Flag
3572dd034e915f493120885d41d546c7
