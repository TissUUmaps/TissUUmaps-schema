#!/usr/bin/env bash
for version in $(tissuumaps-schema versions); do
    mkdir -p _site/${version}
    tissuumaps-schema generate --version ${version} > _site/${version}/schema.json
    generate-schema-doc --config expand_buttons _site/${version}/schema.json _site/${version}/schema_doc.html
done
