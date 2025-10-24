class Solution:
    def decodeString(self, s: str) -> str:
        commands = []
        d = ""
        intt = ""

        for i in s:
            if i.isdigit():
                intt += i 
            elif i == "[":
                commands.insert(0, [intt, ""])
                intt = "" 
            elif i == "]":
                if len(commands) > 1:
                    commands[1][1] += commands[0][1] * int(commands[0][0])
                else:
                    d += commands[0][1] * int(commands[0][0])
                commands.pop(0)
            else:
                if commands:
                    commands[0][1] += i
                else:
                    d += i

        return d

                