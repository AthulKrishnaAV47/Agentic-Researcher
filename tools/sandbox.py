from e2b_code_interpreter import Sandbox
from pydantic import BaseModel, Field
from config import E2B_API_KEY

class SandBoxSchema(BaseModel):
    code: str = Field(description="The code that needs to be executed in Python sandbox. Use print() to display outputs")

def run_python(code: str) -> str:
    if not E2B_API_KEY:
        return "E2B_API_KEY is Missing from the enivronment"

    try:
        with Sandbox.create() as sandbox:
            exe = sandbox.run_code(code)
            output = []

            if exe.logs.stdout:
                output.append(f"STDOUT:\n{'-'*10}\n{''.join(exe.logs.stdout)}\n{'-'*10}")
            if exe.logs.stderr:
                output.append(f"STDERR:\n{'-'*10}\n{''.join(exe.logs.stderr)}\n{'-'*10}")
            if exe.text:
                output.append(f"RESULT:\n{'-'*10}\n{exe.text}\n{'-'*10}")
                
            if exe.error:
                output.append(f"ERROR:\n{'-'*10}\n{exe.error.name}: {exe.error.value}\n{exe.error.traceback}\n{'-'*10}")

            if not output:
                return "Code executed successfully with no output (did you forget to print?)."
                
            return "\n\n".join(output)
    except Exception as e:
        return f"Sandbox Execution failed: {str(e)}"
