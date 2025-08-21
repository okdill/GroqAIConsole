from groq import Groq
k="https://groq.com api key here";c=Groq(api_key=k);h=[];print(f"------------------------------------------------------------------------\nGROQ AI made by okdill on github! Type exit or quit to stop chatting !!\n------------------------------------------------------------------------")
while 1:
    t=input("> ").strip()
    if t.lower()in("exit","quit"):break
    if not t:continue
    h.append({"role":"user","content":t});o=""
    for x in c.chat.completions.create(model="llama3-70b-8192",messages=h,stream=True):
        p=x.choices[0].delta.content or"";print(p,end="",flush=True);o+=p
    print();h.append({"role":"assistant","content":o})
