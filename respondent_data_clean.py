def join_respondents(contact_info_file, other_info_file, output_file):
    import pandas as pd
    res_con = pd.read_csv(contact_info_file)
    res_oth = pd.read_csv(other_info_file)
    respondents = res_con.join(res_oth, on="respondent_id")
    respondents['birthdate'] = respondents['birthdate'].to_datetime(format='%Y-%m-%d')
    return respondents.to_csv(output_file)
#join_respondents