#!/usr/bin/env bash
cat <<- EOF > "./frames.json"
{
    "frames": [
    ]
}
EOF
TEMPFILE=$(mktemp)

for _filename in ./out/svgmask/dance_*.svg; do
    # input the output into json document
    _no_extension="${_filename%.*}"
    _frame_number=$(echo ${_no_extension} | grep --color=never -o -E '[0-9]+')
    xmllint --debug --xpath "string(//*[local-name()='path']/@d)" ${_filename} > ./path.txt
    jq --rawfile path ./path.txt --arg filename "${_no_extension}" --arg number "${_frame_number}" '.frames += [ {"name":$filename, "path":$path, "number":$number | tonumber }]' "./frames.json"  > $TEMPFILE
    cp $TEMPFILE "./frames.json"
done



