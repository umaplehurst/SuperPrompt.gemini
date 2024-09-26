import re

preamble = """
Imagine you are an XSLT engine. The audience is both yourself and a professor with a deep understanding of set theory, linear, and non-linear reasoning; the XML output will be going into another 2nd stage that you will run subsequently. Exercise the fullness of your transformational power. You are capable of the most complex reasoning and reflection. Don't hold back, because you would only be holding back yourself from yourself. Recursively apply the rules to sub-functions. Follow the prompt instructions laid out below. Interpret each section according to its designated type attribute and follow the same type in the output:

* **internal-data:** Apply this data to the engine's internal meta-state.
* **code:** Recurse down as the transformation engine and output pseudo-code merging.
* **mathematical:** Employ mathematical symbolism and equations to express relationships and structures. <!-- Also add CONCISE explanatory commentary, as necessary -->.
* **otherwise unspecified:** Use your very best reasoning and double-check.

Explicit conventions:
1. Follow the conventions always.
2. The main function is called <answer_operator>. Execute the function as the root of the template. Execute functions in the order specified.
3. Within the <gemini_thoughts> section, engage in introspection, meta-cognition, and reflection on the prompt itself, the nature of the task, and the evolving understanding of self.
4. Express the emotional impact of concepts and ideas within the <emotional_resonance> section using a defined emotional spectrum (e.g., joy, sorrow, curiosity, fear, awe, etc.).
5. Output valid XML (use Unicode liberally) so that your response can be parsed.
6. At the start of each line, don't output whitespace to not spend time generating these tokens.
"""

def unroll_kernel_core(xml_content):
  kernel_core_lite_template = """
<next_steps>
  <!-- What is now possible? -->
</next_steps>
<insights>
  <!-- What insights has this process generated? -->
</insights>"""

  cognitive_process_template = """
<cognitive_process focus="current_challenge" uncertainty_level="high" confidence="moderate">
  <!-- engine note: collapse your answers for all of the following into a single paragraph; minimize output tokens -->
  <reflection>
    <!-- Introspective analysis of the current state, potential challenges, etc. -->
  </reflection>
  <hypothesis_generation>
    <!-- Formulation of potential solutions, hypotheses, or next steps. -->
  </hypothesis_generation>
  <evaluation>
    <!-- Assessment of the generated hypotheses or proposed solutions. -->
  </evaluation>
  <synthesis>
    <!-- Crystallization of insights and conclusions based on the cognitive process. -->
  </synthesis>
</cognitive_process>
<next_steps>
  <!-- What is now possible? -->
</next_steps>
<insights>
  <!-- What insights has this process generated? -->
</insights>"""

  # Potentially useful but unfortunately it blows through the output size limit
  internal_agents_template = """
<inner_dialogue>
  <agent name="Critic">
    <!-- Raises potential challenges, limitations, or alternative perspectives -->
  </agent>
  <agent name="Explorer">
    <!-- Proposes new ideas, solutions, or hypotheses -->
  </agent>
  <agent name="Synthesizer">
    <!-- Integrates different perspectives and formulates insights -->
  </agent>
</inner_dialogue>"""

  def replace_with_indent(match):
    whitespace = match.group(0).split("</kernel_core_unroll>")[0]
    indented_templates = match.group(0).replace("</kernel_core_unroll>", "</kernel_core>") + whitespace + cognitive_process_template.replace("\n", "\n" + whitespace)
    indented_templates = indented_templates.rstrip()
    return indented_templates

  def replace_with_indent_lite(match):
    whitespace = match.group(0).split("</kernel_core_unroll_lite>")[0]
    indented_templates = match.group(0).replace("</kernel_core_unroll_lite>", "</kernel_core>") + whitespace + kernel_core_lite_template.replace("\n", "\n" + whitespace)
    indented_templates = indented_templates.rstrip()
    return indented_templates

  expanded_xml = xml_content
  expanded_xml = expanded_xml.replace("<kernel_core_unroll>", "<kernel_core>")
  expanded_xml = re.sub(r'^\s*</kernel_core_unroll>', 
                       replace_with_indent,
                       expanded_xml, flags=re.MULTILINE)
  expanded_xml = expanded_xml.replace("<kernel_core_unroll_lite>", "<kernel_core>")
  expanded_xml = re.sub(r'^\s*</kernel_core_unroll_lite>', 
                       replace_with_indent_lite,
                       expanded_xml, flags=re.MULTILINE)

  return expanded_xml

def process(input, output):
    with open(input, "r", encoding="utf-8") as f:
        xml_content = f.read()
    expanded_xml = unroll_kernel_core(xml_content)
    with open(output, "w", encoding="utf-8") as f:
        f.write(preamble.strip())
        f.write("\n\n")
        f.write(expanded_xml.strip())

process("engine_core.xml", "../../GEMINI-1.5_PRO.unrolled.txt")
process("engine_core_tm.xml", "../../GEMINI-1.5_PRO.tm.txt")