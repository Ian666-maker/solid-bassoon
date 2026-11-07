import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-key"))

class ClientPayload(BaseModel):
    username: str
    role: str
    scores: dict
    overallAverage: int
    goalSummary: str = "Private wealth growth"

@app.post("/api/ai-analyze")
def ai_analyze(data: ClientPayload):
    prompt = f"""
    You are an expert Private Wealth Adviser AI. Analyze this client profile and write a concise, professional 3-sentence executive summary:
    - Client Name: {data.username}
    - Occupation: {data.role}
    - 5 Core Dimension Scores (0-100%): {data.scores}
    - Overall Readiness: {data.overallAverage}%
    - Goal Summary: {data.goalSummary}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        insight_text = response.choices[0].message.content.strip()
    except Exception as e:
        insight_text = f"Executive Summary for {data.username}: Client demonstrates an overall readiness score of {data.overallAverage}%. Immediate adviser review recommended."

    # 【新增】自动发送邮件给 HR 的逻辑
    send_email_to_hr(data.username, data.role, data.scores, data.overallAverage, insight_text)

    return {"status": "success", "insight": insight_text}

def send_email_to_hr(username, role, scores, avg_score, insight):
    # 配置你的邮箱（例如 QQ邮箱、Gmail 或 163邮箱 的 SMTP）
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"  # 你的发送邮箱
    sender_password = "your_app_password"  # 邮箱应用授权码
    hr_email = "hr_target@example.com"      # HR 的接收邮箱

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = hr_email
    msg['Subject'] = f"[FRAME Assessment] New Client Intake: {username} ({role})"

    body = f"""
    New client assessment has been submitted via FRAME Portal:
    
    - Client Name: {username}
    - Role / Occupation: {role}
    - Overall Readiness Score: {avg_score}%
    
    --- 5-Dimension Pentagon Scores ---
    - Goal Clarity: {scores.get('goal_clarity', 0)}%
    - Investment Knowledge: {scores.get('investment_knowledge', 0)}%
    - Risk Comfort: {scores.get('risk_comfort', 0)}%
    - Planning Readiness: {scores.get('planning_readiness', 0)}%
    - Financial Complexity: {scores.get('financial_complexity', 0)}%
    
    --- Executive AI Summary ---
    {insight}
    
    Please log in to the Adviser Command Center to review and record workflow decisions.
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, hr_email, msg.as_string())
        server.quit()
        print("Assessment report successfully emailed to HR!")
    except Exception as e:
        print(f"Email simulation / send note: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)