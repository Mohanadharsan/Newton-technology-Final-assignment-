audio_minutes = 5

asr_cost_per_minute = 2.0     
llm_summary_cost = 5.0        

total_asr_cost = audio_minutes * asr_cost_per_minute
total_cost = total_asr_cost + llm_summary_cost

print("Audio duration:", audio_minutes, "minutes")
print("ASR cost:", total_asr_cost)
print("LLM summarization cost:", llm_summary_cost)
print("Total estimated cost:", total_cost)