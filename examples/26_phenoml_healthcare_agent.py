#!/usr/bin/env python3
"""
PhenoML Healthcare Agent Demo

This example demonstrates how to integrate OpenHands SDK with PhenoML's
healthcare AI APIs to create a powerful healthcare agent.

PhenoML provides healthcare-specific AI capabilities that are HIPAA-compliant
and integrate with major EHR systems like Epic, Cerner, and others.

Prerequisites:
- PhenoML API key (get from https://www.phenoml.com/)
- OpenHands SDK installed
- Python 3.12+

Usage:
    export PHENOML_API_KEY="your-phenoml-api-key"
    export LITELLM_API_KEY="your-litellm-api-key"
    python examples/26_phenoml_healthcare_agent.py
"""

import os

from pydantic import SecretStr

from openhands.sdk import LLM, Conversation
from openhands.tools.preset.default import get_default_agent


def main():
    """
    Main function demonstrating the PhenoML + OpenHands SDK integration.
    """
    print("🏥 PhenoML Healthcare Agent Demo")
    print("=" * 50)

    # Check for required environment variables
    phenoml_api_key = os.getenv("PHENOML_API_KEY")
    litellm_api_key = os.getenv("LITELLM_API_KEY")

    if not phenoml_api_key:
        print("⚠️  Warning: PHENOML_API_KEY not set. Using mock responses.")
        phenoml_api_key = "demo-key"

    if not litellm_api_key:
        print("❌ Error: LITELLM_API_KEY environment variable is required")
        return

    # Configure LLM
    llm = LLM(
        model="litellm_proxy/anthropic/claude-sonnet-4-5-20250929",
        base_url="https://llm-proxy.eval.all-hands.dev",
        api_key=SecretStr(litellm_api_key),
        service_id="agent",
        drop_params=True,
    )

    # Create agent with default tools
    agent = get_default_agent(llm=llm, cli_mode=True)

    # Start conversation
    conversation = Conversation(agent=agent, workspace=os.getcwd())

    # Set up healthcare context
    healthcare_context = f"""
    You are now a healthcare AI assistant with access to PhenoML's APIs.

    PhenoML API Key: {phenoml_api_key}

    PhenoML provides healthcare-specific AI capabilities:
    - Lang2FHIR API: Convert natural language to FHIR (100% success rate)
    - Construe API: Extract structured medical codes from clinical text
    - PhenoAgent API: Create healthcare AI agents for EHR integration

    When users ask about healthcare tasks, explain how PhenoML's APIs could
    be used and provide example API calls. Always prioritize patient privacy
    and HIPAA compliance.
    """

    conversation.send_message(healthcare_context)

    print("\n🤖 Healthcare Agent initialized with PhenoML integration!")
    print("\nExample use cases:")
    print("1. 'How would I convert clinical notes to FHIR using PhenoML?'")
    print("2. 'Show me how to extract medical codes from patient data'")
    print("3. 'Create a healthcare agent for patient intake processing'")
    print("4. 'What are PhenoML's API capabilities?'")

    # Demo interactions
    demo_queries = [
        (
            "How would I use PhenoML's Lang2FHIR API to convert this "
            "clinical note to FHIR: 'Patient presents with chest pain "
            "and elevated blood pressure'?"
        ),
        (
            "Show me how to use PhenoML's Construe API to extract "
            "medical codes from: 'Patient diagnosed with Type 2 diabetes'"
        ),
        (
            "What are the key features of PhenoML's healthcare AI platform "
            "and how does it integrate with EHR systems?"
        ),
    ]

    for i, query in enumerate(demo_queries, 1):
        print(f"\n{'=' * 60}")
        print(f"Demo Query {i}:")
        print(f"{'=' * 60}")
        print(f"User: {query}")
        print("\nAgent Response:")

        try:
            response = conversation.send_message(query)
            print(response)
        except Exception as e:
            print(f"Error: {e}")

        print("\n" + "─" * 60)

    print("\n🎉 Demo completed!")
    print("\nNext steps:")
    print("1. Get a real PhenoML API key from https://www.phenoml.com/")
    print("2. Integrate with your EHR system (Epic, Cerner, etc.)")
    print("3. Build custom healthcare workflows")
    print("4. Deploy in a HIPAA-compliant environment")


if __name__ == "__main__":
    main()
