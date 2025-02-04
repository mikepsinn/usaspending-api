
-- Update recipient locations with data from broker

UPDATE references_location as loc
SET
    address_line1 = broker.legal_entity_address_line1,
    address_line2 = broker.legal_entity_address_line2,
    address_line3 = broker.legal_entity_address_line3,
    city_name = broker.legal_entity_city_name,
    congressional_code = broker.legal_entity_congressional,
    location_country_code = broker.legal_entity_country_code,
    country_name = broker.legal_entity_country_name,
--    county_code = broker.legal_entity_county_code, TODO: Uncomment when fields added to broker
--    county_name = broker.legal_entity_county_name, TODO: Uncomment when fields added to broker
    state_code = broker.legal_entity_state_code,
    state_name = broker.legal_entity_state_descrip,
--    zip5 = broker.legal_entity_zip5, TODO: Uncomment when fields added to broker
--    zip_last4 = broker.legal_entity_zip_last4, TODO: Uncomment when fields added to broker
    zip4 = broker.legal_entity_zip4
FROM fpds_transactions_to_update_location broker,
	transaction_fpds,
	transaction_normalized,
	legal_entity
WHERE  broker.detached_award_proc_unique = transaction_fpds.detached_award_proc_unique
AND transaction_fpds.transaction_id = transaction_normalized.id
AND legal_entity.legal_entity_id = transaction_normalized.recipient_id
AND legal_entity.location_id = loc.location_id
AND broker.le_loc_change = TRUE;



-- Update place of performance locations with data from broker

UPDATE references_location as loc
SET
    city_name = broker.place_of_perform_city_name,
    congressional_code = broker.place_of_performance_congr,
    location_country_code = broker.place_of_perform_country_c,
    country_name = broker.place_of_perf_country_desc,
--    county_code = broker.place_of_perform_county_co, TODO: Uncomment when fields added to broker
    county_name = broker.place_of_perform_county_na,
    state_code = broker.place_of_performance_state,
    state_name = broker.place_of_perfor_state_desc,
--    zip5 = broker.place_of_performance_zip5, TODO: Uncomment when fields added to broker
--    zip_last4 = broker.place_of_perform_zip_last4, TODO: Uncomment when fields added to broker
    zip4 = broker.place_of_performance_zip4a
FROM fpds_transactions_to_update_location broker,
    transaction_fpds,
    transaction_normalized
WHERE  broker.detached_award_proc_unique = transaction_fpds.detached_award_proc_unique
AND transaction_fpds.transaction_id = transaction_normalized.id
AND loc.location_id = transaction_normalized.place_of_performance_id
AND broker.pop_change = TRUE;
