# probability and bayes
p_spam = 0.3
p_free_given_spam = 0.8
p_free_given_ham = 0.1 



spam_emails = 30 
ham_emails = 70

free_in_spam = 30 * 0.8  
free_in_ham = 70 * 0.1

total_free = free_in_spam + free_in_ham
p_free_given_free = free_in_spam / total_free

print(p_free_given_free)


winner_in_spam = 30 * 0.7
money_in_spam = 30 * 0.6
winner_in_ham = 70 * 0.05
money_in_ham = 70 * 0.08

spam_score = free_in_spam * winner_in_spam * money_in_spam
ham_score = free_in_ham * winner_in_ham * money_in_ham

p_spam_given_all = spam_score / (spam_score + ham_score)
print(f"P(spam | free+winner+money) = {p_spam_given_all:.3f}")