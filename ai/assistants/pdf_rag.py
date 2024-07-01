from typing import Optional

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

from ai.settings import ai_settings
from ai.storage import pdf_assistant_storage
from ai.knowledge_base import pdf_knowledge_base


def get_rag_pdf_assistant(
    run_id: Optional[str] = None,
    user_id: Optional[str] = None,
    debug_mode: bool = False,
) -> Assistant:
    """Get a RAG Assistant with a PDF knowledge base."""

    return Assistant(
        name="rag_pdf_assistant",
        run_id=run_id,
        user_id=user_id,
        llm=OpenAIChat(
            model=ai_settings.gpt_4,
            max_tokens=ai_settings.default_max_tokens,
            temperature=ai_settings.default_temperature,
        ),
        storage=pdf_assistant_storage,
        knowledge_base=pdf_knowledge_base,
        # This setting adds references from the knowledge_base to the user prompt
        add_references_to_prompt=True,
        # This setting adds the last 6 messages from the chat history to the API call
        add_chat_history_to_messages=True,
        # Enable monitoring on phidata.app
        # monitoring=True,
        debug_mode=debug_mode,
        description="""
            "I have uploaded a CV file in the data directory. Please parse the CV and extract the required details to return a fully populated ParseCvResponseDto object. Follow these detailed steps:

Load the CV file: Access the file from the data directory.
Extract Personal Information:
First Name: Extract the candidate's first name.
Last Name: Extract the candidate's last name.
Gender: Determine the candidate's gender using the Gender enum values (MALE, FEMALE, OTHERS).
Date of Birth: Extract and format the candidate's date of birth as a Date object.
Email: Extract the candidate's email address.
Phone Code: Extract the international phone code.
Phone Number: Extract the candidate's phone number.
Extract Professional Information:
Title: Extract the candidate's job title.
Summary: Extract a brief summary about the candidate.
Total Years of Experience: Calculate and extract the candidate's total years of experience.
Location: Extract the candidate's current location.
Extract Work Experiences:
For each work experience listed in the CV, extract:
Company Name
Position
From Month
From Year
To Month
To Year
Description
Create an array of CvWorkExperience objects with the above details.
Extract Educational Background:
For each education entry listed in the CV, extract:
Institution
Degree
From Month
From Year
To Month
To Year
Create an array of CvEducation objects with the above details.
Extract Skills: List all the skills mentioned in the CV.
Extract Languages:
For each language listed in the CV, extract:
Label (e.g., English, Spanish)
Level: Determine the proficiency level using the LanguageLevel enum values (BEGINNER, ELEMENTARY, INTERMEDIATE, UPPER_INTERMEDIATE, ADVANCED, FLUENT, NATIVE, CONVERSATIONAL)
Create an array of CvLanguage objects with the above details.
Format the extracted data using the ParseCvResponseDto structure as follows:

typescript
Copy code
@Exclude()
export class CvWorkExperience {
  @Expose()
  companyName: string | null;

  @Expose()
  position: string | null;

  @Expose()
  fromMonth: number | null;

  @Expose()
  fromYear: number | null;

  @Expose()
  toMonth: number | null;

  @Expose()
  toYear: number | null;

  @Expose()
  description: string | null;
}

export class CvLanguage {
  label: string;

  level: LanguageLevel | null;
}

@Exclude()
export class CvEducation {
  @Expose()
  institution: string | null;

  @Expose()
  degree: string | null;

  @Expose()
  fromMonth: number | null;

  @Expose()
  toMonth: number | null;

  @Expose()
  fromYear: number | null;

  @Expose()
  toYear: number | null;
}

@Exclude()
export class ParseCvResponseDto {
  @Expose()
  firstName: string | null;

  @Expose()
  lastName: string | null;

  @Expose()
  gender: Gender | null;

  @Expose()
  dateOfBirth: Date;

  @Expose()
  email: string | null;

  @Expose()
  phoneCode: string | null;

  @Expose()
  phone: string | null;

  @Expose()
  title: string | null;

  @Expose()
  summary: string | null;

  @Expose()
  totalYearOfExperience: number | null;

  @Expose()
  location: string | null;

  @Expose()
  @Type(() => CvWorkExperience)
  workExperiences: CvWorkExperience[];

  @Expose()
  @Type(() => CvEducation)
  educations: CvEducation[];

  @Expose()
  skills: string[];

  @Expose()
  @Type(() => CvLanguage)
  languages: CvLanguage[];
}
        """,
        extra_instructions=[
            "Keep your answers under 3 sentences.",
        ],
        assistant_data={"assistant_type": "rag"},
    )
