import requests
from requests.exceptions import RequestException

from prototypes import Problem

LEETCODE_API_URL = "https://leetcode.com/api/problems/all/"
LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"


def get_all_problems():
    try:
        response = requests.get(LEETCODE_API_URL, timeout=10)
        response.raise_for_status()
    except RequestException as exc:
        raise RuntimeError("No se pudo acceder a la API de LeetCode.") from exc
    data = response.json()
    return data['stat_status_pairs']


def fetch_problem(slug):
    query = '''
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                content
                difficulty
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                exampleTestcases
                sampleTestCase
                metaData
            }
        }
    '''
    variables = {"titleSlug": slug}
    try:
        response = requests.post(
            LEETCODE_GRAPHQL_URL,
            json={"query": query, "variables": variables},
            timeout=10
        )
        response.raise_for_status()
    except RequestException as exc:
        raise RuntimeError(
            "No se pudo acceder a la API GraphQL de LeetCode."
        ) from exc
    question = response.json().get('data', {}).get('question')
    if not question:
        raise ValueError("No se encontró el detalle del ejercicio.")
    code = [snippet['code'] for snippet in question['codeSnippets'] if snippet['langSlug'] == 'python3']
    return Problem(
        id=question['questionId'],
        frontend_id=question['questionFrontendId'],
        title=question['title'],
        slug=question['titleSlug'],
        difficulty=question.get('difficulty', 'Unknown'),
        content=question['content'],
        code=code[0] if code else '',
        example_test_cases=question.get('exampleTestcases', ''),
        sample_test_case=question.get('sampleTestCase', ''),
    )
