import pandas as pd

file1 = pd.read_csv(filepath_or_buffer="E:/Ativs/tcc/projeto py/data/data-2/2018-1.csv", encoding='utf-8', low_memory=False, on_bad_lines='warn')

file_filtered = file1[['contract_award_unique_key','award_id_piid', 'parent_award_agency_id','parent_award_agency_name',
                       'federal_action_obligation','total_dollars_obligated','total_outlayed_amount_for_overall_award', 'base_and_exercised_options_value',
                       'current_total_value_of_award', 'base_and_all_options_value', 'potential_total_value_of_award', 'action_date',
                       'period_of_performance_start_date', 'period_of_performance_current_end_date', 'period_of_performance_potential_end_date',
                       'awarding_agency_name', 'awarding_sub_agency_name', 'object_classes_funding_this_award', 'recipient_uei', 'recipient_duns', 'recipient_name',
                       'recipient_name_raw', 'recipient_doing_business_as_name', 'recipient_city_name', 'recipient_state_code', 'recipient_state_name',
                       'award_type_code', 'award_type', 'type_of_contract_pricing', 'transaction_description', 'product_or_service_code_description',
                       'naics_description', 'domestic_or_foreign_entity', 'commercial_item_acquisition_procedures', 'price_evaluation_adjustment_preference_percent_difference',
                       'multi_year_contract', 'contracting_officers_determination_of_business_size', 'organizational_type',
                       'usaspending_permalink', 'last_modified_date']].copy()

file_filtered.to_csv("E:\\Ativs\\tcc\\projeto py\\py2018-1-filtered.csv", index=False)



