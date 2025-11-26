#!/bin/bash
# Test Supabase connection and schema

SUPABASE_URL="https://pblxazslxcotbdxtvnlb.supabase.co"
SUPABASE_KEY="sb_publishable_mCH6Oiq63NdZAeOct2c80w_v8hHwsuS"

echo "Testing Supabase connection..."
echo ""

# Test extractions table exists
echo "1. Checking extractions table..."
RESPONSE=$(curl -s -w "\n%{http_code}" \
  "${SUPABASE_URL}/rest/v1/extractions?select=count" \
  -H "apikey: ${SUPABASE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_KEY}")

HTTP_CODE=$(echo "$RESPONSE" | tail -n 1)
BODY=$(echo "$RESPONSE" | head -n -1)

if [ "$HTTP_CODE" = "200" ]; then
  echo "   OK - extractions table accessible"
else
  echo "   ERROR - HTTP $HTTP_CODE"
  echo "   Response: $BODY"
  echo ""
  echo "   If 404, you need to run the schema SQL:"
  echo "   1. Go to Supabase > SQL Editor"
  echo "   2. Run: intelligence-dashboard/supabase-schema.sql"
fi

echo ""

# Test insert (then delete)
echo "2. Testing insert capability..."
TEST_ID="test_$(date +%s)"

INSERT_RESPONSE=$(curl -s -w "\n%{http_code}" \
  "${SUPABASE_URL}/rest/v1/extractions" \
  -H "apikey: ${SUPABASE_KEY}" \
  -H "Authorization: Bearer ${SUPABASE_KEY}" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  -d "{
    \"extraction_id\": \"${TEST_ID}\",
    \"source_file_name\": \"test-connection.txt\",
    \"meeting_type\": \"test\",
    \"entities_created\": 0,
    \"completeness_score\": 100,
    \"auto_quality_rating\": \"excellent\"
  }")

INSERT_CODE=$(echo "$INSERT_RESPONSE" | tail -n 1)

if [ "$INSERT_CODE" = "201" ]; then
  echo "   OK - Can insert records"

  # Clean up test record
  curl -s -X DELETE \
    "${SUPABASE_URL}/rest/v1/extractions?extraction_id=eq.${TEST_ID}" \
    -H "apikey: ${SUPABASE_KEY}" \
    -H "Authorization: Bearer ${SUPABASE_KEY}" > /dev/null
  echo "   OK - Test record cleaned up"
else
  echo "   ERROR - HTTP $INSERT_CODE"
  INSERT_BODY=$(echo "$INSERT_RESPONSE" | head -n -1)
  echo "   Response: $INSERT_BODY"
fi

echo ""
echo "Test complete!"
echo ""
echo "If all tests passed, your Supabase is ready."
echo "Next: Set up Zapier workflow using docs/OPERATIONALIZATION-GUIDE.md"
