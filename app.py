from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
user_data={}
@app.route("/", methods=["POST"])
def reply():
    sender=request.values.get("from")
    incoming_msg = request.values.get("Body", "").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()


    if sender not in user_data:
        user_data[sender]= {"step":"start"}
    step = user_data[sender]["step"]

    if step == "start" or incoming_msg.lower() in ["hi","hello","hi i want to know more about your services"]:
        user_data[sender]["step"]="menu"
        msg.body( "Hello👋 Welcome to *Asopa Marketing*!\n\nWe help businesses like yours grow online.\nWhat would you like to do today?. \n\n1 I want Marketing Services\n2 Book Free Call \n3 All Social Media links\n4 Contact \n\n")
   
     #option 1
    elif "1" in incoming_msg or " i want marketing services" in incoming_msg:
         user_data[sender]["step"]="get_business"
         msg.body("Greate!To assist you better please answer a few quick questions.\n\n1.What kind of business do you run?(E.g.,Real Estate,interior Design,Coaching,E-commerce,other)")
    elif step=="get_business":
        user_data[sender]["business"]=incoming_msg 
        user_data[sender]["step"]="get_services" 
        msg.body("\n2.What services are you looking for?\n*OUR SERVICES:*\n- Social Media Marketing\n- Website Development\n- Product Shoots\n- Ad Events\n- Google Ads\n- Meta Ads\n- Social Media Management\n- Digital Content Creation\n- Business Consultancy\n- Business automation")
    elif step =="get_services":
        user_data[sender]["services"]=incoming_msg
        user_data[sender]["step"]="get_budget"
        msg.body("\n3. What's your monthly marketing budget?\nOptions:\nunder 5k\n5k-10k\n10k-20k\n20k-more\nCustom Package Based on your needs\n") 
    elif step =="get_budget":
        user_data[sender]["budget"]=incoming_msg 
        user_data[sender]["step"]="get_goal"
        msg.body("\n4. What's your goal from digital marketing?\nOptions:\nGet more leads\nImprove Branding\nGet sales for my products\nBuild an online presence\n\n")
    elif step =="get_goal":
        user_data[sender]["goal"]=incoming_msg
        user_data[sender]["step"]="done_services"
        msg.body("*Thank you for providing your information!*\n\n" "Here's a quick summary :\n"f"Business:{user_data[sender]['business']}\n"f"Services:{user_data[sender]['services']}\n "f"Budget:{user_data[sender]['budget']}\n"f"Goal:{user_data[sender]['goal']}\n\n""Our team will reach out to you shortly!")
         
         
         #option 2
    elif "2" in incoming_msg or "call" in incoming_msg:
         user_data[sender]["step"]="get_name"
         msg.body("Please enter your *Name* to book your free consultation call.")
    elif step =="get_name":
         user_data[sender]["name"]="incoming_msg"
         user_data[sender]["step"]="get_phone"
         msg.body("*Great!* now enter your *Phone Number*.")
    elif  step =="get_phone":
         user_data[sender]["phone"]="incoming_msg"
         user_data[sender]["step"]="get_email"
         msg.body("Almost done!Please enter your *Email ID*.")
    elif step =="get_email":
         user_data[sender]["email"]="incoming_msg"
         user_data[sender]["step"]="done_call"
         msg.body("*Congratulations!* Your Free consultation call is booked.\n\n" f"Name:{user_data[sender]['name']}\n" f"Phone Number:{user_data[sender]['phone']}\n" f"Email:{user_data[sender]['email']}\n" "Our expert will contact you shortly!")
    
    #option 3
    elif "3" in incoming_msg or "link" in incoming_msg:
         msg.body("*OUR ALL PLATFORMS LINKS ARE:*\n*Instagram*\nhttps://www.instagram.com/asopamarketing/\n*Facebook*\n https://www.facebook.com/share/1a1DZDez9z/\n*LinkedIn*\n https://www.linkedin.com/in/govind-asopa-074567367/\n*What's app chat*\nhttps://wa.me/919309827721?text=Hi%20I%20want%20to%20know%20more%20about%20your%20services\n*Website*\n https://www.asopamarketing.com\n\n")
    
    #option 4 
    elif "4" in incoming_msg or "contact" in incoming_msg:
        msg.body("📞 *Contact Us:*\n*Asopa Marketing*\n*Call:* +91-9284122832,+91-9309827721\n*Email:* hello@asopamarketing.com\n *Website:* https://www.asopamarketing.com\n ")
    
    else:
        msg.body("❓ I didn’t understand that. Reply with:\n1 I want Marketing Services\n2 Book Free Call\n3 All Social Media links\n4 Contact \n\n")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


  
