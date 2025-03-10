from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI()

def classify_file_type(file_content):
    """Determine if a file is claims, membership, or cag type using GPT"""
    try:
        # Create prompt with few-shot examples
        messages = [
            {
                "role": "system", 
                "content": """You are a pharmaceutical data analyst. Classify files as 'claims', 'membership', or 'cag' based on their content.
                Here are some examples:
                File content: MemberID,EnrollDate,PlanType,Gender,DOB
                Classification: membership
                File content: ClaimID,DateOfService,NDC,Quantity,PrescriberNPI
                Classification: claims
                File content: GroupID,ContractType,BenefitYear,FormularyCode
                Classification: cag
                """},
            {"role": "user", "content": f"File content: {file_content}"}
        ]
        # Create prompt with few-shot examples in different messages
        # messages = [
        #     {"role": "system", "content": "You are a pharmaceutical data analyst. Classify files as 'claims', 'membership', or 'cag' based on their content."},
        #     {"role": "user", "content": "File content: MemberID,EnrollDate,PlanType,Gender,DOB"},
        #     {"role": "assistant", "content": "membership"},
        #     {"role": "user", "content": "File content: ClaimID,DateOfService,NDC,Quantity,PrescriberNPI"},
        #     {"role": "assistant", "content": "claims"},
        #     {"role": "user", "content": "File content: GroupID,ContractType,BenefitYear,FormularyCode"},
        #     {"role": "assistant", "content": "cag"},
        #     {"role": "user", "content": f"File content: {file_content}"}
        # ]

        # Get classification from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error classifying file: {str(e)}"

def main():
    # Sample file contents for testing
    file1 = "PatientID,RxNumber,PharmacyID,DrugName,DaysSupply"
    file2 = "SubscriberID,EffectiveDate,TermDate,RelationshipCode"
    file3 = "ContractID,BenefitDesign,CopayTier,NetworkType"

    # Test the classifier with different files
    print(f"File 1 type: {classify_file_type(file1)}")
    print(f"File 2 type: {classify_file_type(file2)}")
    print(f"File 3 type: {classify_file_type(file3)}")

if __name__ == "__main__":
    main() 