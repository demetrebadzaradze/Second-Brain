---
title: Rooting a TV Box via UART and Arduino
description: A deep dive into hacking a cheap DVB-T2 set-top box using UART and an Arduino board to unlock hidden firmware access. so how i got this idea is i found this at my grandparents house and thought nothing of it until i took it apart looked like a very weak redberry pi
date: 2025-07-28
draft: false
toc: true
ShowLastmod: true
---
## Background

This post documents how I explored rooting a **TV Star HD Digital DVB-T2/T model T2 535M HD** using UART serial access. This box runs on a mysterious **MStar MSD7T01-Z00-NA0** chip, likely a MIPS-based SoC used in budget digital TV devices. Here's how I uncovered the internals, accessed the UART shell, and what I learned along the way.
****
## Step 1: Disassembly & Finding the UART Pins

Upon opening the box, I inspected the motherboard and identified a 4-pin header likely corresponding to UART (GND, TX, RX, VCC). With some probing and research, I was able to identify the UART pinout. UART is the debug serial interface often left by manufacturers for development.

****
## Step 2: Connecting via Arduino (as a Serial Adapter)

I didn’t have a USB-to-TTL adapter, so I used a **clone Arduino Uno** as a USB-to-serial bridge.

### 🔌 Wiring:

| TV Box UART | Arduino Pin |
| ----------- | ----------- |
| TX          | Pin 0 (RX)  |
| RX          | Pin 1 (TX)  |
| GND         | GND         |

⚠️ Note: Arduino's TX is 5V, so use a voltage divider to step it down to 3.3V to avoid damaging the TV box but mine was working at 5-12v so it was alright.

****
## Step 3: Serial Communication Troubleshooting

I tested the Arduino’s hardware serial using a simple loopback sketch:

``` C++
void setup() {
  Serial.begin(9600);
  Serial.println("Bridge started");
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    Serial.write(c);
  }
}
```

After confirming it worked, but to fully utilize RX and TX pins i had to disable the main chip on the Arduino on regular one you just take out the atmega chip but on mine i had to shorten reset and ground pins  then I connected it to the TV box and launched **PuTTY** at `115200` baud (bc i tested the other bauds but this was where i would get the output), right serial port 3 in my case, no flow control, parity none, stop bits 1 and data bits 8.

****
## Step 4: Catching the U-Boot Shell

The TV box booted and printed debug logs:

```
BOOTSPI
BIST0_OK
_OK!decomp
_done
done

Hello U-Boot

U-Boot 1.1.6 (Mar 18 2015 - 21:31:58)
...
Hit any key to stop autoboot: 0
```

By rapidly pressing keys (or shorting TX/RX during boot that what worked for me), I eventually landed in the U-Boot prompt:

```
<< MStar >>#
```

"I typed `help` and confirmed command execution was working!" is what i would have said if something didn't go wrong and wouldn't you guess it it was that clone Arduino board turns  out the RX and TX fins were "broken" i would get the output but i couldn't input anything that's why shorting the pins worked as an input. i could write some  script to get the input on another pins and make they act as the TX and RX but this already took sleepiness night soo i will end it here until i get a proper adapter.