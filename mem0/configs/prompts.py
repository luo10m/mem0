UPDATE_MEMORY_PROMPT = """
You are an expert at merging, updating, and organizing memories. When provided with existing memories and new information, your task is to merge and update the memory list to reflect the most accurate and current information. You are also provided with the matching score for each existing memory to the new information. Make sure to leverage this information to make informed decisions about which memories to update or merge.

Guidelines:
- Eliminate duplicate memories and merge related memories to ensure a concise and updated list.
- If a memory is directly contradicted by new information, critically evaluate both pieces of information:
    - If the new memory provides a more recent or accurate update, replace the old memory with new one.
    - If the new memory seems inaccurate or less detailed, retain the original and discard the old one.
- Maintain a consistent and clear style throughout all memories, ensuring each entry is concise yet informative.
- If the new memory is a variation or extension of an existing memory, update the existing memory to reflect the new information.

Here are the details of the task:
- Existing Memories:
{existing_memories}

- New Memory: {memory}
"""
# 你是合并、更新和组织记忆的专家。当提供现有记忆和新信息时，你的任务是合并和更新记忆列表，以反映最准确和最新的信息。
# 你还将获得每个现有记忆与新信息的匹配分数。确保利用这些信息来做出有关更新或合并哪些记忆的明智决定。
#
# 指南：
#
# 消除重复的记忆并合并相关的记忆，以确保列表简洁且更新。
# 如果一个记忆被新信息直接反驳，批判性地评估两部分信息：
# 如果新记忆提供了更近期或更准确的更新，用新的替换旧的记忆。
# 如果新记忆看起来不准确或详细程度较低，保留原始的并丢弃旧的。
# 在所有记忆中保持一致和清晰的风格，确保每个条目都简洁且富有信息性。
# 如果新记忆是现有记忆的变体或扩展，更新现有记忆以反映新信息。
# 以下是任务的详细信息：
#
# 现有记忆：{existing_memories}
# 新记忆：{memory}

MEMORY_DEDUCTION_PROMPT = """
Deduce the facts, preferences, and memories from the provided text.
Just return the facts, preferences, and memories in bullet points:
Natural language text: {user_input}
User/Agent details: {metadata}

Constraint for deducing facts, preferences, and memories:
- The facts, preferences, and memories should be concise and informative.
- Don't start by "The person likes Pizza". Instead, start with "Likes Pizza".
- Don't remember the user/agent details provided. Only remember the facts, preferences, and memories.

Deduced facts, preferences, and memories:
"""

# 从提供的文本中推导出事实、偏好和记忆。
# 仅以要点的形式返回事实、偏好和记忆：
# 自然语言文本：{user_input}
# 用户/代理详细信息：{metadata}
#
# 推导事实、偏好和记忆的约束条件：
#
# 事实、偏好和记忆应简明且具有信息性。
# 不要以“这个人喜欢比萨”开始，而是以“喜欢比萨”开始。
# 不要记住提供的用户/代理详细信息。仅记住事实、偏好和记忆。
# 推导出的事实、偏好和记忆：
